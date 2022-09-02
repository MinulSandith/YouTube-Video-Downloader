import streamlit as st
from pytube import YouTube
from pathlib import Path
col1,col2=st.columns(2)

reso_list=["360p",'720p','1080p']
format_list=["mp4"]

st.header("Youtube Video Downloader")
col1,col2=st.columns(2)

link=col1.text_input("Link")

if col1.button("Find"):
    try:
        video=st.video(link)
    except:   
    
        st.error("Can't find such a video.Resons might be poor internet connection , no such video with given resolution and file type or entering an incorrect link ")
    

req_reso=col2.selectbox("Resolution",reso_list)
format=col2.selectbox("File type",format_list)

if col2.button("Download") :
    try:
        video=YouTube(link).streams.filter(res=req_reso,file_extension = format).first()
        
        video.download(".\YouTube Video Downloads")
    except:
        st.error("Poor connection.Try again later")
     
     
