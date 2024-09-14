import streamlit as st

from postgresql import isLiked, like_a_post, remove_like

def show_card(key, post):
    with st.container(border=True):
        liked = isLiked(post[0], st.session_state.user_email)
        st.image(post[6].tobytes())
        
        col1, col2, col3 = st.columns([5, 1.1, 1], gap="large", vertical_alignment="bottom")
        
        col1.header(post[3])

        col2.text(f"{post[5]} likes")

        if not liked:
            emoji = "♡"
        else:
            emoji = "❤️"

        like_btn = col3.button(emoji, key=key)
        st.write(post[4])

        if like_btn:

            if not liked:
                like_a_post(post[0], st.session_state.user_email)
            else:
                remove_like(post[0], st.session_state.user_email)
            
            st.experimental_rerun()

