import streamlit as st


pg = st.navigation([st.Page("play.py")])
pg.run()
"""
This is a website to demonstrate Streamlit's API.
You can stop looking at this now.

Please.
"""
if 'tama' not in st.session_state:
    st.session_state['tama']= {'Name':'pablo',"type":"monkey",'hunger':0,'thirst':0,'boredness':5}
st.image("image.png")

feed = st.button('Feed tamagotchi')
drink = st.button('Give water to tamagotchi')
if 'number' not in st.session_state:

    st.session_state['number'] = 0

clicked_button = st.button("Press me!")
if clicked_button:
    st.session_state['number'] += 1

st.write(st.session_state['number'])