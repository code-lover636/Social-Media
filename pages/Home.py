import streamlit as st
from streamlit_option_menu import option_menu

from components import Feed, MyPosts, CreatePost, LikedPages


# Constants
TITLE = "PIXELS"


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
if 'access' not in st.session_state:
    st.session_state['access'] = 'denied'


# Navbar
def streamlit_menu():
    selected = option_menu(
        menu_title=None,  # required
        options=["Feed", "My Posts", "Liked Pages", "Create Post"],  # required
        icons=["house", "sticky-fill", "hand-thumbs-up", "plus-lg"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
    )
    return selected

def main():
    selected = streamlit_menu()

    match selected:
        case "Feed":
            Feed.show_feed()
        case "My Posts":
            MyPosts.show_my_posts()
        case "Create Post":
            CreatePost.show_create_post()
        case "Liked Pages":
            LikedPages.show_liked_pages()


if st.session_state['access'] == "denied":
    st.switch_page("Login.py")
else:
    main()
