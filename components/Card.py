import streamlit as st

def show_card(key):
    with st.container(border=True):
        st.image("./image.jpg")
        
        col1, col2 = st.columns([6, 1], gap="large", vertical_alignment="bottom")
        
        col1.header("Rainy Day")

        emoji = "❤"
        like_btn = col2.button(emoji, key=key)
        st.write("Lorem ipsum dolor, sit amet consectetur adipisicing elit. Odio nostrum deserunt suscipit illum rerum sed ex amet error ipsam. Cumque illo quod tenetur, quos ducimus et necessitatibus aut deleniti expedit")

        if like_btn:
            print("liked")
            emoji = "❤️" if emoji == "❤" else "❤️"