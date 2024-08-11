import streamlit as st
import datetime

from database import register_user, login_user


def login_page():

    with st.form('Login'):
        email = st.text_input("Email ID")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button('Log In')
    
    if submit:
        email = email.strip()
        password = password.strip()

        if email == "" or password == "":
            st.warning("All fields must be filled", icon="⚠️")
        elif login_user(email, password):
            return True
        else:
            st.error("Invalid Email or Password", icon="❌")
    
    return False
            


def register_page():
    with st.form('Login'):
        first_name = st.text_input("First Name")
        second_name = st.text_input("Second Name")
        email = st.text_input("Email ID")
        dob = st.date_input("Date Of Birth", min_value=datetime.datetime(1900, 1, 1), max_value=datetime.datetime.now())
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confim Password", type="password")
        submit = st.form_submit_button('Register')
    
    if submit:
        first_name = first_name.strip()
        second_name = second_name.strip()
        email = email.strip()
        password = password.strip()
        confirm_password = confirm_password.strip()
        if first_name == "" or second_name == "" or email == "" or password == "" or confirm_password == "":
            st.warning("All fields must be filled", icon="⚠️")
        elif password != confirm_password:
            st.error("Passwords doesn't match", icon="❌")
        elif register_user(first_name, second_name, email, password, dob):
            return True
        else:
            st.error("Cannot Login. Some error occured", icon="❌")
    
    return False
    