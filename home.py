import streamlit as st

def render_home():
    st.title("Welcome to the Home Page")
    if st.button("Back to Main Page"):
        st.session_state.page = "home"  # Go back to the main page
        # Streamlit will automatically rerun the app after the session state is updated
