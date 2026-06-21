import streamlit as st
import json
from openai import OpenAI
import random


if('play' not in st.session_state):
    st.switch_page('Home.py')


st.set_page_config(page_title="Tamagotchi",page_icon="🙉")

if st.session_state['tama']['type'] == 'bunny':
    #st.image('tama-bunny.gif')
    'bunny'
elif st.session_state['tama']['type'] == 'fish':
    #st.image('tama-fish.gif')
    'fish'
elif st.session_state['tama']['type'] == 'turtle':
    #st.image('tama-turtle.gif')
    'turtle'
elif st.session_state['tama']['type'] == 'egg':
    # st.image('tama-egg.gif')
    'egg'
elif st.session_state['tama']['type'] == 'duck':
    #st.image('tama-duck.gif')
    'duck'


st.write(f""" 
{st.session_state['tama']['name']} is your faithful {st.session_state['tama']['type']} tamagotchi!
their hunger is {st.session_state['tama']['hunger']} and thirst is {st.session_state['tama']['thirst']}
their boredness is {st.session_state['tama']['boredness']}

""")
st.session_state['tama']['event']
feed = ''
drink = ''
play = ''
wash = ''
if st.session_state['tama']['type'] != 'carcass':
    feed = st.button('Feed tamagotchi')
    drink = st.button("Give water to tamagotchi")
    play = st.button("Play with tamagotchi")
    wash = st.button("Wash your tamagotchi")
else:
    redo = st.button("Play again")
    if redo:
        st.session_state['play'] = False
        del st.session_state['tama']
        st.rerun()

if feed and st.session_state['tama']['hunger'] <10:
    st.session_state['tama']['hunger'] +=1
    
if drink and st.session_state['tama']['thirst'] < 10:
    st.session_state['tama']['thirst'] +=1
    
if play and st.session_state['tama']['boredness'] >0:
    st.session_state['tama']['boredness'] -=1
    if st.session_state['tama']['hunger'] > 1 or st.session_state['tama']['thirst'] >1:
        st.session_state['tama']['hunger'] -= 1
        st.session_state['tama']['thirst'] -= 1

if wash and st.session_state['tama']['boredness'] <11:
    st.session_state['tama']['boredness'] +=1
    roll = random.randint(1,2)
    if roll == 1:
        st.session_state['tama']['thirst'] -= 1
    else:
        st.session_state['tama']['hunger'] -=1


if st.session_state['tama']['hunger'] == 0 or st.session_state['tama']['thirst'] == 0:
    st.session_state['type'] = 'carcass'
    st.session_state['tama']['hunger'] = None
    st.session_state['tama']['thirst'] = None
    st.session_state['tama']['boredness'] = None
    st.rerun()

    # 1


event = st.button("Generate random event")

if event:
        

    client = OpenAI(
        api_key = st.secrets["key"]
    )

    # 2
    system_prompt = """
    You are running a virtual pet tamagotchi. This tamagotchi has 3 different stats: hunger, thirst, and boredness.
      each time a user clicks a button you will generate a new event, the event will be of different levels of how important it is. those will be given by the user
      here is an example of how your json tamagotchi representation should be:


  {'name':name,"type":tama_type,'hunger':5,'thirst':5,'boredness':5,
    "event": "event description"} 

    the levels of response from bad to good are catastrophic, bad, ok, good
        

    here are some examples of a runthrough of the program:

    user starting data: {'name':test,"type":"turtle",'hunger':5,'thirst':3,'boredness':6,
    "event":"Welcome and good luck taking care of your pet!"} , good

    assistant response (good): 
        {'name':test,"type":turtle,'hunger':4,'thirst':1,'boredness':3,
          "event": "test the turtle goes for a long swim, this makes them tired and thirsty but much less bored."             }
   
    user starting data: {'name':test,"type":"turtle",'hunger':3,'thirst':2,'boredness':6,
    "event":"Welcome and good luck taking care of your pet!"} , bad

    assistant response (bad): 
        {'name':test,"type":turtle,'hunger':7,'thirst':5,'boredness':8,
          "event": "you eat plastic on accident, this hurts you making you sick, making you very hungry and thirsty."             }
   
    user starting data: {'name':test,"type":"turtle",'hunger':1,'thirst':3,'boredness':10,
    "event":"Welcome and good luck taking care of your pet!"} , ok

    assistant response (ok): 
        {'name':test,"type":turtle,'hunger':2,'thirst':5,'boredness':4,
          "event": "test the turtle takes a nap, making them slgihtly less bored, and slightly more hungry and thirsty" }
    
    user starting data: {'name':test,"type":"turtle",'hunger':2,'thirst':4,'boredness':3,
    "event":"Welcome and good luck taking care of your pet!"} , catastrophic

    assistant response (catastrophic): 
        {'name':"test the dead rabbit","type":'carcass','hunger':None,'thirst':None,'boredness':None,
          "event": "your rabbit went into a bath and came under hypothermic shock, unfortunately passing away"             }
   
   when catastrophic events happen: make sure to make all the stats none and the type 'carcass'
    """

    roll = random.randint(1,100)
    event_type = ''
    if roll < 35:
        event_type = ', good'
    elif roll < 65:
        event_type = ', ok'
    elif roll < 95:
        event_type = ', bad'
    else:
        event_type = ', catastrophic'
    # 3
    user_prompt = json.dumps(st.session_state['tama']) + event_type


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
    st.session_state['tama'] = response
    
    st.rerun()
    
    
    