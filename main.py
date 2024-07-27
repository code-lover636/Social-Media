import streamlit as st
from streamlit_option_menu import option_menu

import database as db
from Pages import Feed, MyPosts, CreatePost


# Constants
TITLE = "PIXELS"


# Page setup
st.set_page_config(
        page_title=TITLE,
        page_icon= "📷"
)

styles = """
<style>
    #stDecoration{
        display: none !important;
    }
</style>
"""

st.markdown(styles, unsafe_allow_html=True)


# Navbar
def streamlit_menu():
    selected = option_menu(
        menu_title=None,  # required
        options=["Feed", "My Posts", "Create Post"],  # required
        icons=["house", "sticky-fill", "plus-lg"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
    )
    return selected


selected = streamlit_menu()


match selected:
    case "Feed":
        Feed.show_feed(selected)
    case "My Posts":
        MyPosts.show_my_posts(selected)
    case "Create Post":
        CreatePost.show_create_post(selected)

# db.add_data("A113", "lost", "conan doyle")
st.table(db.get_data())