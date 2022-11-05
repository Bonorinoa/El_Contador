# Personal Accountant

# DONE: 1) Set up container or virtual environment
# DONE: 2) Find a way to connect via SMS or WhatsApp (Twilio [https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1])
# DONE: 3) Figure out a way to update a dataset based on SMS (text of key:value pair)
# DONE: 4) Setup Streamlit dashboard
# TODO: 5) Brainstorm additional dimensions for spreadsheet
# TODO: 6) Improve streamlit's interface.


# Dependencies: Streamlit (Dashboard, server), Twilio (Phone number creation and SMS reading), 
import os

TWILIO_ACCOUNT_SID = "AC1dc24948a97469cbfe31a00155658764"
TWILIO_AUTH_TOKEN = "1115e0f1268d623c444322394c8e78ba"

os.environ["TWILIO_ACCOUNT_SID"] = TWILIO_ACCOUNT_SID
os.environ["TWILIO_AUTH_TOKEN"] = TWILIO_AUTH_TOKEN

#------------------------------------------------------------------------------
# STREAMLIT DASHBOARD [START]
import streamlit as st

st.title('My Finances')



#------------------------------------------------------------------------------

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import datetime
import time

# Find your Account SID and Auth Token in Account Info and set the environment variables.
# See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

## To send message
#message = client.messages.create(body='Wassap madafaka', 
#                                 from_='+16075243807', 
#                                 to='+17189023213')

messages = client.messages.list(limit=3)

lastMSg = messages[1].body

Category, Cost, TypeTr = lastMSg.split(" ")
current_time = datetime.datetime.now()

# Date: Date of input entry
# Categroy: Category of transaction
# Value: Monetary value of transaction
# Type: Debit (+) or Credit (-)
data_entry = {"Date":[current_time], 
              "Category": [Category], 
              "Value": [float(Cost.replace(",", "."))],
              "Type": [TypeTr]}
st.write(f'Data Entry: {data_entry}')

#--------------------------------------------------------------------------------
# FINANCES SPREADSHEET
import pandas as pd
import numpy as np

message_df = pd.DataFrame(data_entry)

st.write("Welcome back!")


  
#--------------------------------------------------------------------------------
# STREAMLIT DASHBOARD [END]

clean_budget = message_df.loc[:, ~message_df.columns.str.contains('^Unnamed')]
st.dataframe(clean_budget)