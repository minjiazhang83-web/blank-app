import streamlit as st
import json
from openai import OpenAI


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

if feed and st.session_state['tama']['hunger'] >=0:
    st.session_state['tama']['hunger'] -=1
    
if drink and st.session_state['tama']['thirst'] >=0:
    st.session_state['tama']['thirst'] -=1
    
if play and st.session_state['tama']['boredness'] >=0:
    st.session_state['tama']['boredness'] -=1

if wash and st.session_state['tama']['hunger'] <11:
    st.session_state['tama']['boredness'] +=1


    # 1

client = OpenAI(
    api_key = st.secrets("key")
)

# 2
system_prompt = """
You are a dungeon master for a DND game. A user will give you a brief description of the world they are playing in. 

Given a description of the fantasy world, come up with a name and description for each party member, and respond with a JSON in the following format:

{
    "NAME_1": "DESCRIPTION_1",
    "NAME_2": "DESCRIPTION_2"
}
"""

""""""
# 3
user_prompt = input("Describe the world that you will be playing in.")


# 4
response = client.chat.completions.create(
    model="gpt-4o",
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
)

# 5
#(json.loads(response.choices[0].message.content))
""""""