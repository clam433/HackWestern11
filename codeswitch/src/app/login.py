import streamlit as st
from pymongo import MongoClient
import hashlib
import jwt
import datetime

# Secret key for JWT
JWT_SECRET = "your_secret_key"  # Replace this with a strong secret key
JWT_ALGORITHM = "HS256"

# Connect to MongoDB
client = MongoClient("mongodb+srv://christopherl4n:108993mW@codeswitch.5snsl.mongodb.net/?retryWrites=true&w=majority&appName=CodeSwitch")
db = client['CodeSwitch']  # Database name
collection = db['users']  # Collection name

def generate_jwt_token(username):
    """Generates a JWT token for the authenticated user."""
    payload = {
        "username": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expires test_in 1 hour
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token

def render_login():
    st.title("Welcome to the Login Page")

    # Login form
    with st.form(key='login_form'):
        username = st.text_input("Username")
        password = st.text_input("Password", type='password')  # Hide the password input
        
        submit_button = st.form_submit_button("Log In")
        
        if submit_button:
            if username and password:
                # Check if username exists
                user = collection.find_one({"username": username})
                
                if user:
                    # Hash the entered password and compare with the stored hash
                    hashed_password = hashlib.sha256(password.encode()).hexdigest()
                    
                    if user["password"] == hashed_password:
                        # Generate JWT token
                        token = generate_jwt_token(username)
                        
                        # Store token test_in session state
                        st.session_state["jwt_token"] = token
                        st.session_state["logged_in"] = True  # Flag to track successful login

                        # Display success message
                        st.success(f"Welcome back, {username}!")
                    else:
                        st.warning("Incorrect password. Please try again.")
                        st.session_state["logged_in"] = False
                else:
                    st.warning("Username not found. Please check your credentials.")
                    st.session_state["logged_in"] = False
            else:
                st.warning("Please fill test_in both fields.")
                st.session_state["logged_in"] = False

    # Check if the user is logged test_in, then show the button to go to the home page
    if st.session_state.get("logged_in"):
        if st.button("Select your project"):
            st.session_state.page = "projects"  # Redirect to home page
            st.rerun()

    # Navigation buttons
    if st.button("Back to Main Page"):
        st.session_state.page = "main"
        st.rerun() # Go back to the main page
    elif st.button("Don't have an account"):
        st.session_state.page = "signup"  # Go to signup page
        st.rerun()

