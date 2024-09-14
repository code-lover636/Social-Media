import streamlit as st
import time    

from postgresql import add_post



def show_create_post():
    for _ in range(3): st.write("")

    with st.form('create post'):
        title = st.text_input("Post heading")
        description = st.text_area("Description")
        image_file = st.file_uploader("Upload Images", type=['png', 'jpg', 'jpeg', 'gif', 'svg'])
        submit = st.form_submit_button('Post')
    
    if submit:
        if title == "" or description == "" or image_file is None:
            st.warning("All fields must be filled", icon="⚠️")
        else:
            posted_time = time.strftime('%Y-%m-%d %H:%M:%S')
            add_post(title, description, image_file.read(), st.session_state['user_email'], posted_time)
            st.success('Posted', icon="✅")
