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
st.session_state['tama']['event']

feed = st.button('Feed tamagotchi')
drink = st.button("Give water to tamagotchi")
play = st.button("Play with tamagotchi")
wash = st.button("Wash your tamagotchi")

if feed and st.session_state['tama']['hunger'] >0:
    st.session_state['tama']['hunger'] -=1
    
if drink and st.session_state['tama']['thirst'] >0:
    st.session_state['tama']['thirst'] -=1
    
if play and st.session_state['tama']['boredness'] >0:
    st.session_state['tama']['boredness'] -=1

if wash and st.session_state['tama']['boredness'] <11:
    st.session_state['tama']['boredness'] +=1


    # 1


event = st.button("Generate random event")

if event:
        

    client = OpenAI(
        api_key = st.secrets["key"]
    )

    # 2
    system_prompt = """
    You are running a virtual pet tamagotchi. This tamagotchi has 3 different stats: hunger, thirst, and boredness. each time a user clicks a button you will generate a new event, make 60% of the events good, 20% ok, 10% bad, 10% catastrophic. for each event return a new json object of how the stats changed as well as a description:



  {'name':name,"type":tama_type,'hunger':0,'thirst':0,'boredness':5,
    "event": "event description"}
        

    here are some examples:

    user starting data: {'name':test,"type":"turtle",'hunger':3,'thirst':2,'boredness':6,
    "event":"Welcome and good luck taking care of your pet!"}

    assistant response: 
        {'name':test,"type":turtle,'hunger':5,'thirst':5,'boredness':4,
          "event": "test the turtle goes for a long swim, this makes them tired and thirsty but less bored."             }
   
    """

    
    # 3
    user_prompt = json.dumps(st.session_state['tama'])


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
    response = (json.loads(response.choices[0].message.content))
    st.session_state['tama'] = response['tama']
    
    st.rerun()
    
    
    