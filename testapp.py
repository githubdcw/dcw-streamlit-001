import streamlit as st
from mylib import *
def xxx(a,c):
  if a == 0:
    a = 1
    c.write(a)
  else:
    a = 0
    c.write(a)
  return    

c = st.container()
a=0
c.write(a)
st.button('Click',on_click=xxx,kwargs={
        'a': a, 'c': c
    })

st.write(add(1,2))
st.write('akira')
if st.button('Say hello'):
  st.write('Hi Akira')
else:
  st.write('Goodbye AK')
  
  

