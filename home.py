import streamlit as st
import jwt
import os
from src.compile import translate


def render_page():
    st.title("Hello World")
    
    if st.button("Logout"):
    # Clear session state related to login
        if "jwt_token" in st.session_state:
            del st.session_state["jwt_token"]  # Remove the JWT token
        if "logged_in" in st.session_state:
            del st.session_state["logged_in"]  # Remove the login status flag
        
        st.session_state.page = "main"  # Go back to the main page

    txt = st.text_area(
        "Text to translate *",
        "",
    )

    with st.expander("Select language to translate from:"):
        from_language = st.selectbox(
            'Select language to translate from: *',
            ('English', 'French', 'New+'),
            key="from_language_selector"
        )
        if from_language == 'New+':
            new_from_language = st.text_input(
                "Enter new language *",
                key="new_from_language",
                help="You must specify a new language if 'New+' option is selected"
            )
            new_from_dialect = st.text_input(
                "Enter a dialect",
                key="new_from_dialect",
                help="Optional"
            )
            generate_keywords_source = st.button("Generate Keywords", key="source_generate")

            if generate_keywords_source:
                if not new_from_language:
                    st.warning("Please enter a source language")

    with st.expander("Select language to translate to:"):
        to_language = st.selectbox(
            'Select language to translate to:',
            ('English', 'French', 'New+'),
            key="to_language_selector"
        )
        if to_language == 'New+':
            new_to_language = st.text_input(
                "Enter new language *",
                key="new_to_language",
                help="You must specify a new language if 'New+' option is selected"
            )
            new_to_dialect = st.text_input(
                "Enter a dialect",
                key="new_to_dialect",
                help="Optional"
            )
            generate_keywords_output = st.button("Generate Keywords", key="output_generate")

            if generate_keywords_output:
                if not new_to_language:
                    st.warning("Please enter an output language")

    if st.button("Translate"):
        if not txt:
            st.error("Text to translate is required")
        elif from_language == '':
            st.error("Source language must be selected")
        elif from_language == 'New+' and not new_from_language:
            st.error("Please specify the new source language")
        elif to_language == '':
            st.error("Output language must be selected")
        elif to_language == 'New+' and not new_to_language:
            st.error("Please specify the new output language")
