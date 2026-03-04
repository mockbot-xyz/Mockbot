# Text-to-Speech (TTS)

Mockbot uses the **Bark AI** model to read out generated sentences.

Because routing TTS audio directly through a headless Python terminal is impractical, Mockbot uses a "Web Overlay" instead. This functions similarly to Streamlabs or StreamElements alerts.

## Core Commands

*   `!mockbot tts on` / `!mockbot tts off`
    *   Turn Text-to-Speech entirely on or off for your channel. When enabled, all generated Markov messages will be spoken.
*   `!mockbot set voice <preset_name>`
    *   Change the voice the bot uses. Available Bark presets look like this: `v2/en_speaker_1`, `v2/en_speaker_9`, etc.

## Putting the Bot on Stream

To hear the bot and display real-time channel variables, you just need to add the OBS overlay to your streaming software.

1. Open **OBS Studio**.
2. Add a new **Browser Source**.
3. Set the **URL** to: `http://localhost:5050/overlay/<your_channel_name>` (Replace `<your_channel_name>` with your actual Twitch name, e.g., `http://localhost:5050/overlay/firestarman`).
4. Set the **Width/Height** to `800x600`.
5. Check **"Control Audio via OBS"** if you want to be able to adjust the bot's volume from your audio mixer.
