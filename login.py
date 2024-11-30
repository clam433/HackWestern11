import streamlit as st
from pymongo import MongoClient
import hashlib

# Connect to MongoDB
client = MongoClient("mongodb+srv://christopherl4n:108993mW@codeswitch.5snsl.mongodb.net/?retryWrites=true&w=majority&appName=CodeSwitch")
db = client['CodeSwitch']  # Database name
collection = db['users']  # Collection name

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
                        # Successful login
                        st.write(f"Welcome back, {username}!")
                        st.session_state.page = "home"  # Redirect to home page after login
                    else:
                        st.warning("Incorrect password. Please try again.")
                else:
                    st.warning("Username not found. Please check your credentials.")
            else:
                st.warning("Please fill in both fields.")
    
    if st.button("Back to Main Page"):
        st.session_state.page = "main"  # Go back to the main page
    elif st.button("Don't have an account"):
        st.session_state.page = "signup"  # Go to signup page

