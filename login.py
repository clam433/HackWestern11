import streamlit as st

def render_page():
    st.title("Welcome to the Login")

    if st.button("Don't have an accout"):
        st.session_state.page = "signup"