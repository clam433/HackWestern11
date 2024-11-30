import streamlit as st
import home  # Import the home.py file

def main():
    # Include the custom CSS
    with open("main.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Landing page logic
    if "page" not in st.session_state:
        st.session_state.page = "home"

    if st.session_state.page == "home":
        st.title("CodeSwitch")
        if st.button("Go to home"):
            st.session_state.page = "home_page"  # Update state to navigate to the home page
            # No need for st.experimental_rerun(), Streamlit will automatically rerun after the state changes
    elif st.session_state.page == "home_page":
        home.render_home()  # Call the function in home.py to render home page content

if __name__ == '__main__':
    main()
