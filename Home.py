import streamlit as st
"""
This is a website to demonstrate Streamlit's API.
You can stop looking at this now.

Please.
"""
#duck, fish, turtle, egg, bunny
col1, col2, col3 = st.columns(3)

with col1:
    st.header('Duck')

    choose_duck = st.button('Choose duck egg')

    st.header("Egg")

    choose_egg = st.button('Choose egg egg')

with col2:
    st.header('Fish')
    choose_fish = st.button("Choose fish egg")

    st.header("Bunny")

    choose_bunny = st.button('Choose Bunny egg')


with col3:
    st.header('Turtle')
    choose_turtle = st.button("Choose turtle egg")
