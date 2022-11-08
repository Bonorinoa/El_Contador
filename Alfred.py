# Personal Accountant
# Dependencies: Streamlit (Dashboard, server)


# DONE: 1) Set up container or virtual environment
# DONE: 2) Find a way to connect via SMS or WhatsApp (Twilio [https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1])
# DONE: 3) Figure out a way to update a dataset based on SMS (text of key:value pair)
# DONE: 4) Setup Streamlit dashboard
# TODO: 5) Brainstorm additional dimensions for spreadsheet
# TODO: 6) Improve streamlit's interface.


#------------------------------------------------------------------------------
# STREAMLIT DASHBOARD [START]
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from update_budget import get_last_text, create_database, update_database, show_database

st.title('El Contador: Mainframe')

# To avoid re-reading database
if 'Read' not in st.session_state:
    st.session_state['Read'] = False
    
    
    
#--------------------------------------------------------------------------------
# STREAMLIT DASHBOARD [Page 1]
st.write("Latest message:")
st.write(get_last_text())

with st.form("create_budget_form"):
    ## Create or initialize database
    new_df = create_database("Contadurias.csv")
    
    # Every form must have a submit button.
    created = st.form_submit_button("Create Database")
    if created:
        st.write("New Database", new_df)
    
with st.form("show_budget_form"):
    current_budget = show_database("Contadurias.csv")

    # Every form must have a submit button.
    show = st.form_submit_button("Show Current Budget")
    if show:
        st.write("Current Budget \n", current_budget)

with st.form("update_budget_form"):
    # Update database.
    # This should trigger when message comes in
    updated_df = update_database("Contadurias.csv")
    
    # Every form must have a submit button.
    updated = st.form_submit_button("Updated")
    if updated:
        st.write("Updated Database", updated_df)

#--------------------------------------------------------------------------------
