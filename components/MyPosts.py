import streamlit as st
from postgresql import fetch_my_posts
from components.Card import show_card

def show_my_posts():
    posts = fetch_my_posts(st.session_state['user_email'])
    for i in range(len(posts)):
        show_card(i, posts[i])
        st.write("")
        st.write("")
        st.write("")