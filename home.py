import streamlit as st
import jwt
def render_page():
    st.title("Hello World")

    if st.button("Logout"):
    # Clear session state related to login
        if "jwt_token" in st.session_state:
            del st.session_state["jwt_token"]  # Remove the JWT token
        if "logged_in" in st.session_state:
            del st.session_state["logged_in"]  # Remove the login status flag
        
        st.session_state.page = "main"  # Go back to the main page
