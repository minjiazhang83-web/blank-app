import streamlit as st

st.set_page_config(page_title="Tamagotchi",page_icon="🐵")
st.image("image.png")
st.write(f""" 
{st.session_state['tama']['name']} is your faithful {st.session_state['tama']['type']} tamagotchi!
their hunger is {st.session_state['tama']['hunger']} and thirst is {st.session_state['tama']['thirst']}
their boredness is {st.session_state['tama']['boredness']}

""")

feed = st.button('Feed tamagotchi')
