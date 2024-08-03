import streamlit as st
from streamlit_option_menu import option_menu

from components import LoginRegister

# Constants
TITLE = "PIXELS | Login"


# Page setup
st.set_page_config(
        page_title=TITLE,
        page_icon= "📷",
        initial_sidebar_state="collapsed"
)

styles = """
<style>
    #stDecoration{
        display: none !important;
    }
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
"""

st.markdown(styles, unsafe_allow_html=True)

# Navbar
def streamlit_menu():
    selected = option_menu(
        menu_title=None,  # required
        options=["Login", "Register"],  # required
        default_index=0,  # optional
        orientation="horizontal",
    )
    return selected


selected = streamlit_menu()


match selected:
    case "Login":
        enter = LoginRegister.login_page()
        st.session_state['access'] = 'granted'
        if enter: st.switch_page("pages/Home.py")

    case "Register":
        enter = LoginRegister.register_page()
        st.session_state['access'] = 'granted'
        if enter: st.switch_page("pages/Home.py")

