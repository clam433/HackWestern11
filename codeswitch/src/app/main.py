import streamlit as st
import codeswitch.src.app.signup as signup  # Import the signup.py file
import login  # Import the login.py file
import home
import jwt  # PyJWT for JWT handling
import datetime

# Secret key for JWT
JWT_SECRET = "your_secret_key"  # Replace this with your actual secret key
JWT_ALGORITHM = "HS256"

def verify_jwt(token):
    """Verify and decode the JWT token."""
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token  # Return decoded data if valid
    except jwt.ExpiredSignatureError:
        st.warning("Session expired. Please log in again.")
        return None
    except jwt.InvalidTokenError:
        st.warning("Invalid token. Please log in.")
        return None

def main():
    # Include the custom CSS
    with open("main.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Landing page logic
    if "page" not in st.session_state:
        st.session_state.page = "main"  # Default to 'main' page if not set

    # Page navigation logic
    if st.session_state.page == "main":
        st.title("CodeSwitch")
        if st.button("Signup"):
            st.session_state.page = "signup"  # Navigate to the signup page
        if st.button("Login"):
            st.session_state.page = "login"  # Navigate to the login page
    elif st.session_state.page == "signup":
        signup.render_home()  # Render signup page content
    elif st.session_state.page == "login":
        login.render_login()  # Render login page content
    elif st.session_state.page == "home":
        # Check for JWT token before rendering the home page
        if "jwt_token" in st.session_state:
            token = st.session_state["jwt_token"]
            decoded_token = verify_jwt(token)  # Verify the token
            if decoded_token:
                # Token is valid, proceed to render the home page
                home.render_page()
            else:
                # Invalid token, redirect to login
                st.session_state.page = "login"
        else:
            # No token found, redirect to login
            st.warning("You need to log in to access this page.")
            st.session_state.page = "login"

if __name__ == '__main__':
    main()
