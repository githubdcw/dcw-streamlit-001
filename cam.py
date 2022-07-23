import streamlit as st
from streamlit_webrtc import webrtc_streamer
import cv2
st.title('Webcam Test')
run = st.checkbox('Run')

import av


def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    flipped = img[::-1,:,:]

    return av.VideoFrame.from_ndarray(flipped, format="bgr24")


webrtc_streamer(key="example", video_frame_callback=video_frame_callback)

# FRAME_WINDOW = st.image([])
# cap = cv2.VideoCapture(1)
# webrtc_streamer(key="example")
# while run:
#   webrtc_streamer(key="example")
#   ret, frame = cam.read()
#   FRAME_WINDOW.image(frame)
# else:
#   st.write('STOPPED')
