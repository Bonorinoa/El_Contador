# FINANCES SPREADSHEET
import pandas as pd
import numpy as np
import csv
import parse_sms

'''
import mysql.connector
from getpass import getpass
from mysql.connector import connect, Error

# TODO: Connect SQL database

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
    ) as connection:
        print(connection)
except Error as e:
    print(e)
'''    

# TODO: Write entry each time a message comes in
# TODO: Open csv only once per session ("On==True")

data_entry = parse_sms.get_message()
data_df = pd.DataFrame(data_entry, index=[0])

def get_last_text():
     
    '''Returns a dictionary with the text infor
    '''
    
    return data_entry

def create_database(filename):
    
    '''Creates a new database with last message recorded and returns pandas dataframe
    '''
    
    with open(filename, 'w') as new_db:
        writer = csv.DictWriter(new_db, fieldnames=('Date', 'Category', 'Value', 'Type'))
        writer.writeheader()
        writer.writerow(data_entry)
        
    return "Created!"

def update_database(filename):
    
    ''' Just boring csv for now
    '''

    message_df = pd.read_csv(filename)
    
    updated_df = pd.concat([message_df, data_df], ignore_index=True)
    
    updated_df.to_csv(filename)
    
    new_db = pd.read_csv(filename)
    
    clean_budget = new_db.loc[:, ~new_db.columns.str.contains('^Unnamed')]
    
    return clean_budget


print(get_last_text())