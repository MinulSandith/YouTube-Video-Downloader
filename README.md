# YouTube Video Downloader

A simple [Streamlit](https://streamlit.io/) web app for previewing and downloading
YouTube videos in a chosen resolution and file format.

## Features

- Paste a YouTube link and preview it in the browser
- Choose a resolution (360p / 720p / 1080p) and file type (mp4)
- Download the video straight to your browser via a `Download` button
  (works on any OS — no hardcoded save paths)

## Requirements

- Python 3.9+
- [pytubefix](https://pypi.org/project/pytubefix/) — an actively maintained
  fork of `pytube`. The original `pytube` package frequently breaks because
  YouTube changes its internal player/cipher logic and `pytube` is patched
  infrequently; `pytubefix` tracks those changes much more actively.

## Setup

```bash
git clone https://github.com/MinulSandith/YouTube-Video-Downloader.git
cd YouTube-Video-Downloader
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
streamlit run main.py
```

This opens the app in your browser (default: http://localhost:8501).

1. Paste a YouTube video link and click **Find** to preview it.
2. Choose the resolution and file type.
3. Click **Download**, then use the **Save video** button that appears to
   save the file to your device.

## Troubleshooting

- **"No stream found for resolution ..."** — not every video is available
  in every resolution/format combination. Try a different resolution.
- **Download or lookup errors** — YouTube periodically changes its internal
  APIs, which can temporarily break extraction libraries like `pytubefix`.
  Try upgrading it: `pip install -U pytubefix`.
- Some videos (age-restricted, private, or region-locked) cannot be
  downloaded due to YouTube's own restrictions.

## Disclaimer

Only download videos you own or have the right to download, in accordance
with YouTube's Terms of Service and applicable copyright law.
