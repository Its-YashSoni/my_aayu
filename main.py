import streamlit as st
from streamlit_option_menu import option_menu
import home

st.set_page_config(
        page_title="AAYU",
        page_icon="logo.jpg",
        layout="centered"

)



class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='MAIN MENU',
                options=['Home'],
                icons=['house-fill'],
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'#02ab21'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "black"},}
                
                )

        
        if app == "Home":
            home.app()
                  
             
    run()