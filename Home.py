import streamlit as st
import random

left_co, cent_co, right_co = st.columns([1,2,1])

with cent_co:
    """
    ## Welcome to Minjias Magical Tamagotchi store!

    *Pick an egg

    *Choose a name

    *Begin an adventure with your new friend!
    """
#duck, fish, turtle, egg, bunny
col1, col2, col3, col4, col5 = st.columns(5)
if 'type' in st.session_state:
    tama_type = st.session_state['type'] 
if 'play' in st.session_state and st.session_state['play']:
    st.switch_page('play.py')

with col1:
    st.header('Duck')

    st.image('duck_egg.gif')

    choose_duck = st.button('Choose duck egg')



with col2:
    st.header('Fish')

    
    
    st.image('Fish_egg.gif')


    choose_fish = st.button("Choose fish egg")



with col3:
    st.header('Turt.')
    st.image('turtle_egg.png')
    choose_turtle = st.button("Choose turtle egg")

with col5:
    st.header("Egg")

    st.image('egg_egg.png')


    choose_egg = st.button('Choose egg egg')

with col4:
    st.header("Bunny")

    st.image('bunny_egg.gif')

    choose_bunny = st.button('Choose Bunny egg')

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
            st.session_state['tama'] = {'name':name,'type':st.session_state['type'],'hunger':random.randint(3,9),'thirst':random.randint(3,9),'boredness':2,'event':'Welcome and good luck taking care of your pet!'}
            st.session_state['play'] = True
            st.rerun()
