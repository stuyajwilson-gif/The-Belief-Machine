# The Belief Machine — Talking Avatar

## 1. Install Python packages

```bash
pip install -r requirements.txt
```

You also need FFmpeg available to MoviePy. On Windows, install FFmpeg and
add it to PATH. On macOS:

```bash
brew install ffmpeg
```

On Ubuntu/Debian:

```bash
sudo apt install ffmpeg
```

## 2. Put the portrait beside the app

Keep the supplied image as:

```text
17080.png
```

in the same folder as `app.py`.

## 3. Run

```bash
streamlit run app.py
```

The browser will open a chat interface.

## 4. Upgrade to real lip-sync

The included animation is deliberately lightweight. For realistic speech,
replace `make_talking_video()` with a neural talking-head model such as
LivePortrait, Wav2Lip or SadTalker, or connect a hosted avatar API.

The application architecture is already separated so that the avatar
renderer can be swapped without rebuilding the chat interface.
