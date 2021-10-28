import streamlit as st
from mylib import *
import dataclasses
def persistent_game_state(initial_state):
    session_id = st.report_thread.get_report_ctx().session_id
    session = st.server.server.Server.get_current()._get_session_info(session_id).session
    # object2 = object1
    # modify object2 then object is modified as well
    # They are mapped to the same memory.
    st.write('in presistent')
    if not hasattr(session, '_gamestate'):
        st.write('no gamestate')
        setattr(session, '_gamestate', initial_state)
    else:
        st.write('has gamestate')
        st.write(st.server.server.Server.get_current()._get_session_info(session_id).session._gamestate)
        st.write(session._gamestate)

    return session._gamestate
def xxx(a,c):
  if a.number == 0:
    a.number = 1
    c.empty()
    c.text(a.number)
#     st.write(state)
#     st.write(a)
  else:
    a.number = 0
    c.empty()
    c.text(a.number)
  return    

@dataclasses.dataclass
class GameState:
    number: int
    num_guesses: int = 0
    game_number: int = 0
    game_over: bool = False

state = persistent_game_state(initial_state=GameState(0))

c = st.empty()
c.text(state.number)
st.button('Click',on_click=xxx,kwargs={
        'a': state,  'c': c
    })

st.write(add(1,2))
st.write('akira')
if st.button('Say hello'):
  st.write('Hi Akira')
else:
  st.write('Goodbye AK')
  
  

