# Setup Guide

## Prerequisites

- **Python 3.8+**
- **NVIDIA GPU** (Highly recommended for TTS)
- **Twitch Account** for the bot

## Step-by-Step

1.  **Run Setup Script**
    ```bash
    ./launch.sh setup
    ```
    This creates the virtual environment and installs core dependencies.

2.  **Install TTS Dependencies (Optional)**
    If you want the bot to speak:
    ```bash
    ./launch.sh setup-tts
    ```
    *Note: This downloads ~3GB of models (PyTorch, Transformers).*

3.  **Configure Credentials**
    Open `settings.conf`:
    *   `tmi_token`: Get this from [https://twitchapps.com/tmi/](https://twitchapps.com/tmi/) (exclude 'oauth:' if the generator provides it, or include it, the bot handles both).
    *   `nickname`: The exact username of the bot account.
    *   `owner`: Your twitch username (for admin commands).
    *   `channels`: Comma-separated list of channels to join.

4.  **Launch**
    ```bash
    ./launch.sh cli
    ```

## Maintenance

- **Logs**: View logs with `./launch.sh logs`
- **Backup**: `./launch.sh backup` (Saves DB and config)
- **Update**: `./launch.sh update-deps`
