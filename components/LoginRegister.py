import streamlit as st

def isValidLogin():
    return True


def isValidNewUser():
    return True

def login_page():

    with st.form('Login'):
        email = st.text_input("Email ID")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button('Log In')
    
    if submit:
        if isValidLogin():
            st.success('Posted', icon="✅")
            return True
        else:
            st.warning("All fields must be filled", icon="⚠️")
            


def register_page():
    with st.form('Login'):
        username = st.text_input("User Name")
        email = st.text_input("Email ID")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confim Password", type="password")
        submit = st.form_submit_button('Register')
    
    if submit:
        if isValidNewUser():
            st.success('Posted', icon="✅")
            return True
        else:
            st.warning("All fields must be filled", icon="⚠️")
    