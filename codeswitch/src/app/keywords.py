import streamlit as st
import pandas as pd

class KeywordsTable:
    def __init__(self, data):
        self.data = pd.DataFrame(data)
        self.render_table()
    
    def render_table(self):
        self.data = st.data_editor(self.data, num_rows="dynamic")

        if st.button("Save changes"):
            print(self.data)
