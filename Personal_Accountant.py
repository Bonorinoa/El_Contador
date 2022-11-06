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
from update_budget import get_last_text, create_database, update_database

st.title('My Finances')

# To avoid re-reading database
if 'Read' not in st.session_state:
    st.session_state['Read'] = False
    
    
    
#--------------------------------------------------------------------------------
# STREAMLIT DASHBOARD [END]

st.write(get_last_text())

# Create or initialize database
new_df = create_database("Contadurias.csv")
st.write(new_df)



# Update database.
# This should trigger when message comes in
updated_df = update_database("Contadurias.csv")
st.write(updated_df)


# PLot updated distribution of values
fig, ax = plt.subplots()
ax.hist(updated_df['Value'], bins=20)

st.pyplot(fig)