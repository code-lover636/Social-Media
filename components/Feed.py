import streamlit as st

def card(key):
    with st.container(border=True):
        st.image("./image.jpg")

        col1, col2 = st.columns([6, 1], gap="large", vertical_alignment="bottom")
        
        col1.header("Rainy Day")
        col2.button("❤️", key=key)
        st.write("Lorem ipsum dolor, sit amet consectetur adipisicing elit. Odio nostrum deserunt suscipit illum rerum sed ex amet error ipsam. Cumque illo quod tenetur, quos ducimus et necessitatibus aut deleniti expedit")

def show_feed(selected):
    st.title(f"You have selected {selected}")
    for i in range(10): 
        card(i)
        st.write("")
        st.write("")
        st.write("")