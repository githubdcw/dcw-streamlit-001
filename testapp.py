import streamlit as st
from mylib import *
def xxx(a,b,c):
  st.write(b)
  b= b+1
  if a == 0:
    a = 1
    c.empty()
    c.text(a)
  else:
    c.empty()
    c.text(a)
  return    

c = st.empty()
a=0
b=0
c.text(a)
st.button('Click',on_click=xxx,kwargs={
        'a': a, 'b':b, 'c': c
    })

st.write(add(1,2))
st.write('akira')
if st.button('Say hello'):
  st.write('Hi Akira')
else:
  st.write('Goodbye AK')
  
  

