import streamlit as st
from postgresql import fetch_liked_posts
from components.Card import show_card

def show_liked_pages():
    posts = fetch_liked_posts(st.session_state.user_email)
    if posts:
        for i in range(len(posts)): 
            show_card(i, posts[i])
            st.write("")
            st.write("")
            st.write("")