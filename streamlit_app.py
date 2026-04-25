import streamlit as st


pg = st.navigation([st.Page("home.py"),st.Page("play.py")])

pg.run()