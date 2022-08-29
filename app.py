
import streamlit as st
from pages import home
from multipage import MultiPage
from pages import machine_learning

st.set_page_config(page_title="ML", page_icon=":tiger:", layout="wide")


app = MultiPage()

# add applications
app.add_page('Home', home.app)
app.add_page('Machine Learning', machine_learning.app)

# Run application
if __name__ == '__main__':
    app.run()