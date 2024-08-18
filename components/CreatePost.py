import streamlit as st

from postgresql import add_post

def show_create_post(selected):
    for i in range(1): st.write("")
    st.title(f"You have selected {selected}")
    for i in range(3): st.write("")

    with st.form('create post'):
        title = st.text_input("Post heading")
        description = st.text_area("Description")
        image_file = st.file_uploader("Upload Images", type=['png', 'jpg', 'jpeg', 'gif', 'svg'])
        submit = st.form_submit_button('Post')
    
    if submit:
        if title == "" or description == "" or image_file is None:
            st.warning("All fields must be filled", icon="⚠️")
        else:
            add_post(title, description, image_file)
            st.success('Posted', icon="✅")
