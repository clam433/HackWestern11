import token
import streamlit as st
import jwt

from app.login import JWT_ALGORITHM, JWT_SECRET
from db.db import get_users_projects


def extract_id():
    try:
    # Decode the JWT token to get the payload
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        # Extract the username from the payload
        username = payload.get("username")
        id = payload.get("id")
        return id
    except jwt.ExpiredSignatureError:
        st.warning("Session expired. Please log in again.")
        return None
    except jwt.InvalidTokenError:
        st.warning("Invalid token. Please log in again.")
        return None

def render_projects(id):
    m = st.markdown("""
                    <style>
                    div.stButton > button:first-child {
                        background-color: #0099ff;
                        color:#ffffff;
                    }
                    div.stButton > button:hover {
                        background-color: #ffffff;
                        color:#0099ff;
                        border-decoration: none;
                        }
                    </style>""", unsafe_allow_html=True)
    st.markdown("""
        <h1 style='font-size: 60px; color: #4A90E2; text-align: center; margin-bottom: 10px;'>
            Projects
        </h1>
        """, unsafe_allow_html=True)
    if st.button("Logout"):
        if "jwt_token" in st.session_state:
            del st.session_state["jwt_token"]  # Remove the JWT token
        if "logged_in" in st.session_state:
            del st.session_state["logged_in"]  # Remove the login status flag  # Go back to the main page
        st.session_state.page = "login"
        st.rerun()

    count = 0
    for project in get_users_projects(id):
        count += 1
        with st.expander("Project " + str(count)):
            user_list = project.get_projects_users()
            user_string = ", ".join(user_list)
            st.write(f"Users: {user_string}")
            st.write("Language: " + project.get_projects_language())

            if st.button("Select project", key=count):
                st.session_state.page = "home"
                st.rerun()
