# FINANCES SPREADSHEET
import streamlit as st
import pandas as pd
import numpy as np
import csv
import time
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
        writer.writerow(parse_sms.get_message())
        
    return "Created!"

def show_database(filename):
    '''Show the Current Budget
    '''
    with open(filename, mode='r') as budget:
        csv_reader = csv.DictReader(budget)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                res = (f'Column names are: {", ".join(row)}')
                line_count += 1
            res += (f'Spent {row["Value"]} on {row["Date"]} for {row["Category"]}.')
            line_count += 1
        res += (f'\nProcessed {line_count} lines.')
    
    return res

def update_database(filename):
    
    ''' Just boring csv for now
    '''

    #with open(filename, 'a') as old_db:
        
    #    writer = csv.writer(old_db)
    #    writer.writerow(data_df.values)


    #message_df = pd.read_csv(filename)
    
    #updated_df = pd.concat([message_df, data_df], ignore_index=True)
    
    data_df.to_csv(filename, mode='a', header=False, index=False)
    
    new_db = pd.read_csv(filename)
    
    clean_budget = new_db.loc[:, ~new_db.columns.str.contains('^Unnamed')]
    
    return clean_budget


print(get_last_text())