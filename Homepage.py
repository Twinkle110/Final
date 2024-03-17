import streamlit as st
import importlib.util
from streamlit_option_menu import option_menu

import Chatbot
import TA_Picture_GPT
import PDF_GPT
import home

# Define a function to import and run a page script dynamically
def run_page(page_name):
    spec = importlib.util.spec_from_file_location(page_name, f"pages/{page_name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.main()

# Configure Streamlit page
#st.set_page_config(
 #   page_title="TA Chatbot",
  #  page_icon="🤖",
#)

# Define page names and their corresponding display names
def run():
    with st.sidebar:
        app = option_menu(
            menu_title='Talent Analytics AI Bot',
            options=['home','Chatbot', 'TA Picture GPT', 'PDF GPT'],
            icons=['house-fill','wechat', 'images', 'filetype-pdf'],
            menu_icon='chat-text-fill',
            default_index=0,  # Set default index to 0 (Chatbot)
            styles={
                "container": {"padding": "5!important", "background-color": 'black'},
                "icon": {"color": "white", "font-size": "23px"},
                "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                             "--hover-color": "blue"},
                "nav-link-selected": {"background-color": "#02ab21"},
            }
        )

    if app == 'home':
        home.app()
    if app == 'Chatbot':
        Chatbot.app()
    elif app == 'TA Picture GPT':
        TA_Picture_GPT.app()
    elif app == 'PDF GPT':
        PDF_GPT.app()

run()
              