import streamlit as st
from mylib import *
def xxx(a,c):
  if a == 0:
    c.write('1')
    a = 1
  else:
    c.write('0')
    a = 0
  return    

c = st.contrainer()
a=0
st.button('Click',on_click=xxx,kwargs={
        'a': a, 'c': c
    })

st.write(add(1,2))
st.write('akira')
if st.button('Say hello'):
  st.write('Hi Akira')
else:
  st.write('Goodbye AK')
  
  

