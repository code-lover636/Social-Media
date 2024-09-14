import streamlit as st

from postgresql import fetch_all_posts
from components.Card import show_card


def show_feed():
    posts = fetch_all_posts()  
    for i in range(len(posts)):
        show_card(i, posts[i])
        st.write("")
        st.write("")
        st.write("")