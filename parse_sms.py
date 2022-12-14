# Dependencies: Twilio (Phone number creation and SMS reading), 
import os
import logging

TWILIO_ACCOUNT_SID = "AC1dc24948a97469cbfe31a00155658764"
TWILIO_AUTH_TOKEN = "1115e0f1268d623c444322394c8e78ba"

os.environ["TWILIO_ACCOUNT_SID"] = TWILIO_ACCOUNT_SID
os.environ["TWILIO_AUTH_TOKEN"] = TWILIO_AUTH_TOKEN

# Find your Account SID and Auth Token in Account Info and set the environment variables.
# See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
#------------------------------------------------------------------------------

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import datetime
import time

def get_message(acc_sid=account_sid, auth_tok=auth_token):
    
    client = Client(acc_sid, auth_tok)
    is_note = False
    is_invoice = False
    ## To send message
    #message = client.messages.create(body='Wassap madafaka', 
    #                                 from_='+16075243807', 
    #                                 to='+17189023213')

    messages = client.messages.list(limit=5)
    current_time = datetime.datetime.now()
    lastMsg = messages[1].body

    if lastMsg.startswith("note"):
        logging.info("Note entry")
        is_note = True
        
        note_text = lastMsg.split(" -> ")[1]
        data_entry = {"Date": current_time, 
                      "Note": note_text}
    
    elif lastMsg.startswith("invoice"):
        logging.info("Invoice entry")
        is_invoice = True
        
        msgElements = [element for element in lastMsg.split(" ")]
        
        if len(msgElements) == 3:
            # Date: Date of input entry
            # Categroy: Category of transaction
            # Value: Monetary value of transaction
            # Type: Debit (+) or Credit (-)
            data_entry = {"Date": current_time, 
                        "Category": Category, 
                        "Value": float(Value.replace(",", ".")),
                        "Type": TypeTr}
        
        # Other cases?
    
    
       
    ## In case we have to update more than one message
    # n: number of days between message date and today (i.e., date of update)
    n = (data_entry['Date'] - current_time).days
    
    if n > 1:
        
        remainingMSgs = messages[1:n].body
        
        data_entries = []
        for msg in remainingMSgs:
            if lastMsg.startswith("note"):
                logging.info("Note entry")
                is_note = True
        
                Category, Value, TypeTr = lastMsg.split(" -> ")[1]
    
            elif lastMsg.startswith("invoice"):
                logging.info("Invoice entry")
                is_invoice = True
                
                msgElements = [element for element in lastMsg.split(" ")]
                current_time = datetime.datetime.now()
                
                if len(msgElements) == 3:
                    # Date: Date of input entry
                    # Categroy: Category of transaction
                    # Value: Monetary value of transaction
                    # Type: Debit (+) or Credit (-)
                    data_entry = {"Date": current_time, 
                                "Category": Category, 
                                "Value": float(Value.replace(",", ".")),
                                "Type": TypeTr}

            data_entries.append(data_entry)
    
        return data_entries


    return data_entry