import streamlit as st

from components.Card import show_card

def show_my_posts(selected):
    st.title(f"You have selected {selected}")
    for i in range(10): 
        show_card(i)
        st.write("")
        st.write("")
        st.write("")