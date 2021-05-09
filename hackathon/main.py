import streamlit as st
from another import xx
import pandas as pd
from database import data

if __name__=="__main__":
    st.title("federico Scraper")
    email = st.text_input('Enter your email')
    url = st.text_input('Enter url for product')
    price = st.text_input('Enter desired price to get notified')
    x=pd.read_csv("C:/Users/39338/Downloads/customer.csv")
    series_obj = pd.Series([url,email,price,],
                           index=x.columns)
    xx = x.append(series_obj,
                          ignore_index=True)
    xx.to_csv("C:/Users/39338/Downloads/customer.csv",index=False)
    st.write('oki,we will notify you ,when the price is right')
