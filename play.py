import streamlit as st

if('play' not in st.session_state):
    st.switch_page('Home.py')


st.set_page_config(page_title="Tamagotchi",page_icon="🐵")
st.image("image.png")
st.write(f""" 
{st.session_state['tama']['name']} is your faithful {st.session_state['tama']['type']} tamagotchi!
their hunger is {st.session_state['tama']['hunger']} and thirst is {st.session_state['tama']['thirst']}
their boredness is {st.session_state['tama']['boredness']}

""")

feed = st.button('Feed tamagotchi')
drink = st.button("Give water to tamagotchi")
play = st.button("Play with tamagotchi")
wash = st.button("Wash your tamagotchi")

if feed:
    st.session_state['tama']['hunger'] -=1
    
if drink:
    st.session_state['tama']['thirst'] -=1
    
if play:
    st.session_state['tama']['boredness'] -=1

if wash:
    st.session_state['tama']['boredness'] +=1


    