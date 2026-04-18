import streamlit as st
from openai import OpenAI

"""
# Translate
Come here for all your translation needs
"""


client = OpenAI(api_key=st.secrets["key"])

system_prompt = "You are a translator. REspond with the sentence, phrase, or word that the user wants you to translate only."


with st.form("language"):
    lang = st.text_input('What language do you want to translate to?')

    text = st.text_input(f"What text do you want to be translated to {lang}")

    b = st.form_submit_button('Submit')
    if b:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=[
                {"role":'system','content':system_prompt},
                {"role":"user","content": f"Translate '{text}' into the language {lang}"}
            ]
        )

        st.write(response.choices[0].message.content)