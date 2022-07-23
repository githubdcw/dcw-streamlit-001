import streamlet as st
import cv2
st.title('Webcam Test')
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
cap = cv2.VideoCapture(1)
while run:
  ret, frame = cam.read()
  FRAME_WINDOW.image(frame)
else:
  st.write('STOPPED')
