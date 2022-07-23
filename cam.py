import streamlit as st
from streamlit_webrtc import webrtc_streamer
import cv2
st.title('Webcam Test')
run = st.checkbox('Run')
# FRAME_WINDOW = st.image([])
# cap = cv2.VideoCapture(1)
while run:
  webrtc_streamer(key="example")
#   ret, frame = cam.read()
#   FRAME_WINDOW.image(frame)
else:
  st.write('STOPPED')
