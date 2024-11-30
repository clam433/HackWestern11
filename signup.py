import streamlit as st
from pymongo import MongoClient
import hashlib


# Connect to MongoDB
client = MongoClient("mongodb+srv://christopherl4n:108993mW@codeswitch.5snsl.mongodb.net/?retryWrites=true&w=majority&appName=CodeSwitch")
db = client['CodeSwitch']  # Database name
collection = db['users']  # Collection name

def render_home():
    st.title("Welcome to the Signup Page")
    
    # Sign-up form
    with st.form(key='signup_form'):
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type='password')  # Hide the password input
        
        submit_button = st.form_submit_button("Sign Up")
        
        if submit_button:
            if username and email and password:
                
                # Check if username or email already exists
                if collection.find_one({"username": username}):
                    st.warning("Username already exists. Please choose a different one.")
                elif collection.find_one({"email": email}):
                    st.warning("Email already registered. Please use a different one.")
                else:
                    # Hash the password before storing
                    hashed_password = hashlib.sha256(password.encode()).hexdigest()
                    
                    # Insert the user data into MongoDB
                    user_data = {
                        "username": username,
                        "email": email,
                        "password": hashed_password
                    }
                    
                    # Insert the data into the 'users' collection
                    result = collection.insert_one(user_data)
                    
                    # Confirm sign-up
                    st.write(f"Sign-up successful! User ID: {result.inserted_id}")
                    # Set the page to 'login' after successful signup
                    st.session_state.page = "login"
            else:
                st.warning("Please fill in all fields.")

    if st.button("Back to Main Page"):
        st.session_state.page = "main"  # Go back to the main page
    elif st.button("Have an Account"):
        st.session_state.page = "login"
