import os
import shutil
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import torch

# PYTORCH 2.6 FIX: Monkey-patch torch.load to use weights_only=False globally for fairseq compatibility
_original_torch_load = torch.load
def _patched_torch_load(*args, **kwargs):
    if 'weights_only' not in kwargs:
        kwargs['weights_only'] = False
    return _original_torch_load(*args, **kwargs)
torch.load = _patched_torch_load

from rvc_python.infer import RVCInference
import logging

app = FastAPI(title="Mockbot RVC Internal API")

# Global RVC Inference context
# This holds the PyTorch CUDA footprint persistently instead of allocating per-request!
device_str = "cuda:0" if torch.cuda.is_available() else "cpu:0"
rvc_engine = RVCInference(device=device_str)

class InferRequest(BaseModel):
    input_path: str
    model_name: str
    pitch: int = 0
    index_rate: float = 0.75

@app.post("/api/infer")
async def process_audio(req: InferRequest):
    if not req.model_name:
        raise HTTPException(status_code=400, detail="Missing RVC model name.")

    # Strip .pth suffix just in case the UI supplied the literal file name
    clean_name = req.model_name[:-4] if req.model_name.endswith('.pth') else req.model_name
    
    pth_path = os.path.abspath(f"voices/{clean_name}.pth")
    index_path = os.path.abspath(f"voices/{clean_name}.index")
    
    if not os.path.exists(pth_path):
        raise HTTPException(status_code=404, detail=f"Model not found at {pth_path}")

    idx = index_path if os.path.exists(index_path) else ""
    tmp_output = req.input_path + ".rvc.tmp.wav"
    
    try:
        global rvc_engine
        
        # Only invoke load_model if the requested .pth differs from the active VRAM cache
        if rvc_engine.current_model != req.model_name:
            logging.info(f"RVC CACHE MISS: Mismatched VRAM weights! Swapping to {req.model_name}.pth")
            # Clear old memory if present before loading new
            if rvc_engine.current_model is not None:
                rvc_engine.unload_model()
            rvc_engine.load_model(model_path_or_name=pth_path, index_path=idx, version="v2")
        else:
            logging.info(f"RVC CACHE HIT: Fast-tracking audio generation using {req.model_name}.pth")
            
        rvc_engine.set_params(
            f0up_key=req.pitch,
            index_rate=req.index_rate,
            f0method="rmvpe"
        )
        
        rvc_engine.infer_file(os.path.abspath(req.input_path), os.path.abspath(tmp_output))

        if not os.path.exists(tmp_output):
             raise HTTPException(status_code=500, detail="RVC generated no output file.")

        return {"status": "success", "tmp_file": tmp_output}

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    # Start the standalone worker on port 5051 natively
    uvicorn.run(app, host="127.0.0.1", port=5051)
