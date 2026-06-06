import streamlit as st
"""
Welcome to Minjias Magical Tamagotchi store!

*Pick an egg

*Choose a name

*Begin an adventure with your new friend!
"""
#duck, fish, turtle, egg, bunny
col1, col2, col3 = st.columns(3)
if 'type' in st.session_state:
    tama_type = st.session_state['type'] 
if 'play' in st.session_state and st.session_state['play']:
    st.switch_page('play.py')

with col1:
    st.header('Duck')

    #st.image('duck_egg.png')

    choose_duck = st.button('Choose duck egg')

    st.header("Egg")

    
    st.image('Egg.gif')

    choose_egg = st.button('Choose egg egg')

with col2:
    st.header('Fish')

    #st.image('fish_egg.png')

    choose_fish = st.button("Choose fish egg")


    st.header("Bunny")

    #st.image('bunny_egg.png')

    choose_bunny = st.button('Choose Bunny egg')


with col3:
    st.header('Turtle')
    choose_turtle = st.button("Choose turtle egg")

if choose_bunny:
    st.session_state['type'] = 'bunny'
    "Bunny"
if choose_fish:
    st.session_state['type']='fish'
    "Fish"
if choose_turtle:
    st.session_state['type']='turtle'
    "Turtle"
if choose_egg:
    st.session_state['type']='egg'
    "Egg"
if choose_duck:
    st.session_state['type']='duck'
    "Duck"


with st.form("new-tama"):
    name = st.text_input("What would you like to name your new pet!")


    sub = st.form_submit_button("Submit name and hatch egg")

    if sub:
        if 'tama' not in st.session_state:
            st.session_state['tama'] = {'name':name,'type':st.session_state['type'],'hunger':0,'thirst':0,'boredness':0,'event':'Welcome and good luck taking care of your pet!'}
            st.session_state['play'] = True
            st.rerun()
