import tempfile

import streamlit as st
from pytubefix import YouTube

RESOLUTIONS = ["360p", "720p", "1080p"]
FILE_TYPES = ["mp4"]

st.header("YouTube Video Downloader")

col1, col2 = st.columns(2)

link = col1.text_input("Link")

if col1.button("Find"):
    if not link:
        st.error("Please enter a YouTube link.")
    else:
        try:
            st.video(link)
        except Exception as exc:
            st.error(f"Can't find such a video. {exc}")

resolution = col2.selectbox("Resolution", RESOLUTIONS)
file_type = col2.selectbox("File type", FILE_TYPES)

if col2.button("Download"):
    if not link:
        st.error("Please enter a YouTube link.")
    else:
        try:
            with st.spinner("Fetching video..."):
                yt = YouTube(link)
                stream = yt.streams.filter(
                    res=resolution, file_extension=file_type
                ).first()

            if stream is None:
                st.error(
                    f"No stream found for resolution {resolution} "
                    f"and file type {file_type}."
                )
            else:
                with tempfile.TemporaryDirectory() as tmp_dir:
                    with st.spinner("Downloading..."):
                        file_path = stream.download(output_path=tmp_dir)
                    with open(file_path, "rb") as f:
                        st.success("Download ready!")
                        st.download_button(
                            label="Save video",
                            data=f,
                            file_name=f"{yt.title}.{file_type}",
                            mime="video/mp4",
                        )
        except Exception as exc:
            st.error(f"Download failed: {exc}")
