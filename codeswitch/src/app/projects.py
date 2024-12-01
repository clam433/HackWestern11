import streamlit as st

class ProjectList:
    def __init__(self, projects):
        self.projects = projects

    def render_projects(self):
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

        for project in self.projects:
            with st.expander(project.getProjectName()):
                user_list = project.getUserList()
                user_string = ", ".join(user_list)
                st.write(f"Users: {user_string}")
                st.write("Language: " + project.getLanguage())

                if st.button("Select project", key=project.getProjectName()):
                    st.session_state.page = "home"
                    st.rerun()
