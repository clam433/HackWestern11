import streamlit as st

def render_page():
    st.title("Hello World")

    if st.button("Back to Main Page"):
        st.session_state.page = "main"  # Go back to the main page