import streamlit as st
import signup  # Import the signup.py file
import login  # Import the login.py file
import home

def main():
    # Include the custom CSS
    with open("main.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Landing page logic
    if "page" not in st.session_state:
        st.session_state.page = "main"  # Default to 'main' page if not set

    if st.session_state.page == "main":
        st.title("CodeSwitch")
        if st.button("Signup"):
            st.session_state.page = "signup"  # Update state to navigate to the signup page
    elif st.session_state.page == "signup":
        signup.render_home()  # Call the function in signup.py to render signup page content
    elif st.session_state.page == "login":
        login.render_login()  # Call the login page rendering logic when page is 'login'
    elif st.session_state.page == "home":
        home.render_page()  # Call the login page rendering logic when page is 'login'

if __name__ == '__main__':
    main()
