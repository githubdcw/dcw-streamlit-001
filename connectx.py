import random, string
from kaggle_environments import evaluate, make, utils
global env
global trainer
global obs
global done
import streamlit as st
import random
import dataclasses

# from gamestate import persistent_game_state
def persistent_game_state(initial_state):
    session_id = st.report_thread.get_report_ctx().session_id
    session = st.server.server.Server.get_current()._get_session_info(session_id).session
    # object2 = object1
    # modify object2 then object is modified as well
    # They are mapped to the same memory.
    st.write('in presistent')
    session
    if not hasattr(session, '_gamestate'):
        st.write('no gamestate')
        setattr(session, '_gamestate', initial_state)
    else:
        st.write('has gamestate')
        st.write(st.server.server.Server.get_current()._get_session_info(session_id).session._gamestate)
        st.write(session._gamestate)

    return session._gamestate

  
HI = 1000

@dataclasses.dataclass
class GameState:
    number: int
    num_guesses: int = 0
    game_number: int = 0
    game_over: bool = False
    env: make("connectx", debug=True)

state = persistent_game_state(initial_state=GameState(random.randint(1, 1000)))

if st.button("NEW GAME"):
    state.number = random.randint(1, HI)
    state.num_guesses = 0
    state.game_number += 1
    state.game_over = False
#     env = make("connectx", debug=True)
    trainer = state.env.train([None, agent_q3])
    obs = trainer.reset()
#     done = False


    

