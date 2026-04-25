import streamlit as st
"""
This is a website to demonstrate Streamlit's API.
You can stop looking at this now.

Please.
"""

types = ['turtle','duck','fish','egg','rabbit']
with st.form("make-tama"):
    tama_type = st.selectbox("Select Tamagotchi type",types)

    name = st.text_input("Enter name here")

    submit = st.form_submit_button("Create and play!")

    if submit:

        if 'tama' not in st.session_state:
            st.session_state['tama']= {'name':name,"type":tama_type,'hunger':0,'thirst':0,'boredness':5}

if st.session_state['play']:
    st.switch_page('play.py')


