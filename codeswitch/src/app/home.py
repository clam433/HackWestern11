import streamlit as st
from code_editor import code_editor
from app.keywords import KeywordsTable

def home_page(lang="python", do_plain_text_edit=False):
    popup = st.empty()

    # Create a sidebar for the fixed elements
    # Text area test_in the sidebar
    if do_plain_text_edit:
        txt = st.text_area(
            "Code Editor",
            placeholder="Enter code here...",
            height=600
        )
    else:
        editor_buttons = [
            {
                "name": "Copy",
                "feather": "Copy",
                "hasText": True,
                "alwaysOn": True,
                "commands": [
                    "copyAll",
                    [
                        "infoMessage",
                        {
                            "text": "Copied to clipboard!",
                            "timeout": 2500,
                            "classToggle": "show"
                        }
                    ]
                ],
                "style": {
                    "top": "-0.25rem",
                    "right": "0.4rem"
                }
            },
            {
                "name": "Shortcuts",
                "feather": "Type",
                "class": "shortcuts-button",
                "hasText": True,
                "commands": [
                    "toggleKeyboardShortcuts",
                    [
                        "conditionalExecute",
                        {
                            "targetQueryString": "#kbshortcutmenu",
                            "condition": True,
                            "command": [
                                "infoMessage",
                                {
                                    "text": "VSCode keyboard shortcuts",
                                    "timeout": 2500,
                                    "classToggle": "show"
                                }
                            ]
                        }
                    ]
                ],
                "style": {
                    "bottom": "calc(50% + 1.75rem)",
                    "right": "0.4rem"
                }
            },
            {
                "name": "Collapse",
                "feather": "Minimize2",
                "hasText": True,
                "commands": [
                    "selectall",
                    "toggleSplitSelectionIntoLines",
                    "gotolinestart",
                    "gotolinestart",
                    "backspace"
                ],
                "style": {
                    "bottom": "calc(50% - 1.25rem)",
                    "right": "0.4rem"
                }
            },
            {
                "name": "Save",
                "feather": "Save",
                "hasText": True,
                "commands": [
                    "save-state",
                    [
                        "response",
                        "saved"
                    ]
                ],
                "response": "saved",
                "style": {
                    "bottom": "calc(50% - 4.25rem)",
                    "right": "0.4rem"
                }
            },
            {
                "name": "Run",
                "feather": "Play",
                "primary": True,
                "hasText": True,
                "showWithIcon": True,
                "commands": [
                    "submit"
                ],
                "style": {
                    "bottom": "0.44rem",
                    "right": "0.4rem"
                }
            },
            {
                "name": "Command",
                "feather": "Terminal",
                "primary": True,
                "hasText": True,
                "commands": [
                    "openCommandPallete"
                ],
                "style": {
                    "bottom": "3.5rem",
                    "right": "0.4rem"
                }
            }
        ]
        response_dict = code_editor(
            code="",
            ghost_text="Enter code here...",
            height="600px",
            lang=lang,
            focus=True,
            buttons=editor_buttons,
            theme="dark",
            shortcuts="vscode"
        )

    # Expandable sections for the dynamic elements
    with st.sidebar:
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

    with st.sidebar:
        to_language = st.selectbox(
            'Select language to translate to: *',
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

