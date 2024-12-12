#Description: This is a stock market dashboard to show some charts and data on some stock

#Import the libraries
import streamlit as st
import pandas as pd
from PIL import Image

#Add a title and an image
st.write("""
# Stock Market Web Application
Visually show data on a stock! Date range from March 25, 2020 to March 25, 2021
""")
image = Image.open("C:\Users\User\Desktop\stockwebapp\download.png")
st.image(image, use_column_width = True)

#Create a sidebar header
st.sidebar.header('User Input')

#Create a function to get users input
def get_input():
    start_date = st.sidebar.text_input("Start Date", "2020-03-25")
    end_date = st.sidebar.text_input("End Date", "2021-03-25")
    stock_symbol = st.sidebar.text_input("Stock Symbol", "Tata Motors")
    return start_date,end_date,stock_symbol

#Create a function to get the company name
def get_company_name (symbol):
    if symbol == 'TATA MOTORS':
        return 'Tata Motors'
    elif symbol == 'VODAFONE IDEA':
        return  'Vodafone Idea'
    elif symbol=='JSW STEEL':
        return 'JSW Steel'
    else :
        'None'

#Create a function to get the proper company data and the proper timeframe from the users start date to the users end date
def get_data(symbol, start, end):
    #Load the data
    if symbol.upper() == 'TATA MOTORS':
        df = pd.read_csv("C:\Users\User\Desktop\stockwebapp\TATAMOTORS.csv")
    elif symbol.upper() == 'VODAFONE IDEA':
        df = pd.read_csv("C:\Users\User\Desktop\stockwebapp\IDEA.csv")
    elif symbol.upper() == 'JSW STEEL':
        df = pd.read_csv("C:\Users\User\Desktop\stockwebapp\JSWSTEEL.csv")
    else:
        df = pd.DataFrame(columns=['Date','Open','High','Low','Close','Adj Close','Volume'])

    #Get the date range
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    #Set the start and end index rows both to 0
    start_row = 0
    end_row = 0

    # Start the date from the top of the data set and go down to see if the users start date is less than or equal to the date in the data set
    for i in range(0, len(df)):
        if start <= pd.to_datetime(df['Date'][i] ):
            start_row = i
            break

    # Start from the bottom of the data set and go up to see if the users end date is greater than or equal to the date in the data set
    for j in range(0, len(df)):
        if end >= pd.to_datetime(df['Date'][len(df) - 1 - j]):
            end_row = len(df) - 1 - j
            break

    # Set the index to be the date
    df = df.set_index(pd.DatetimeIndex(df['Date'].values))

    return df.iloc[start_row:end_row + 1, :]

#Get the user input
start, end, symbol = get_input()
#Get the data
df = get_data(symbol, start, end)
#Get the company name
company_name = get_company_name(symbol.upper())

#Display the close price
st.header(company_name + "Close price \n")
st.line_chart(df['Close'])

#Display the volume
st.header(company_name + "Volume \n")
st.line_chart(df['Volume'])

#Get statistics on the data
st.header('Data statistics')
st.write(df.describe())

