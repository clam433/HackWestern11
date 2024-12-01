import streamlit as st
from keywords import KeywordsTable

def render_page():
    popup = st.empty()

    # Create a sidebar for the fixed elements
    with st.sidebar:
        st.markdown("""
            <h1 style='font-size: 40px; text-align: left; color: #4A90E2; margin-bottom: 0px;'>
                Hello World
            </h1>
            """, unsafe_allow_html=True)
        
        if st.button("Logout"):
        # Clear session state related to login
            if "jwt_token" in st.session_state:
                del st.session_state["jwt_token"]  # Remove the JWT token
            if "logged_in" in st.session_state:
                del st.session_state["logged_in"]  # Remove the login status flag  # Go back to the main page
        
        # Text area in the sidebar
        txt = st.text_area(
            "Text to translate *",
            "",
            height=150
        )

    # Expandable sections for the dynamic elements
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
                else:
                    with popup.container():
                        KeywordsTable({
                        'Name': ['John', 'Jane', 'Bob', 'Alice', 'timbuktu','aaaaaa','aaaaaa','aaaaa'],
                        'Age': [29, 30, 35, 28, 222, 21, 223, 22],
                        'City': ['New York', 'London', 'Paris', 'Tokyo', 'timbuktu','aaaaaa','aaaaaa','aaaaa'],
                        'CItay': ['New York', 'London', 'Paris', 'Tokyo', 'timbuktu','aaaaaa','aaaaaa','aaaaa'],
                        'CiITA': ['New York', 'London', 'Paris', 'Tokyo', 'timbuktu','aaaaaa','aaaaaa','aaaaa'],
                        'Cityyyyy': ['New York', 'London', 'Paris', 'Tokyo', 'timbuktu','aaaaaa','aaaaaa','aaaaa'],
                        'Citydssss': ['New York', 'London', 'Paris', 'Tokyo', 'timbuktu','aaaaaa','aaaaaa','aaaaa'],
                    })

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
                else:
                    with popup.container():
                        KeywordsTable({
                        'Name': ['John', 'Jane', 'Bob', 'Alice'],
                        'Age': [29, 30, 35, 28],
                        'City': ['New York', 'London', 'Paris', 'Tokyo'],
                        'CItay': ['New York', 'London', 'Paris', 'Tokyo'],
                        'CiITA': ['New York', 'London', 'Paris', 'Tokyo'],
                        'City': ['New York', 'London', 'Paris', 'Tokyo'],
                        'City': ['New York', 'London', 'Paris', 'Tokyo'],
                    })

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