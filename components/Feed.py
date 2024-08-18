import streamlit as st

from postgresql import fetch_all_posts
from components.Card import show_card


def show_feed(selected):
    st.title(f"You have selected {selected}")
    posts = fetch_all_posts()
    # print(posts)
    for i in range(10): 
        show_card(i)
        st.write("")
        st.write("")
        st.write("")