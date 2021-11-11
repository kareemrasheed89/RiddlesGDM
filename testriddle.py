import streamlit as st
from time import sleep

def is_game_active():
    if 'game_active' in st.session_state.keys() and st.session_state['game_active']:
        return True
    else:
        return False

if is_game_active():
    # TODO: implement logic to fetch random_question (and options) on each rerun
    res = st.selectbox('random_question', ['a','b','c','d'])
    if st.button('confirm'):
        st.session_state['random_question'] = res # saves answers for each random question in sesion state for future reference
        st.info('you chose option: ' + res)
        sleep(1)
        st.experimental_rerun()
else:
    if st.button('start game'):
        st.session_state['game_active'] = True
        st.experimental_rerun()
st.write(st.session_state)
