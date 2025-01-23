import streamlit as st
import pandas as pd
import numpy as np

# Title 
st.title("Welcome to Streamlit")


# display message
st.write("This is test message")
st.write("This simple easy frame work")

df = pd.DataFrame({"K1":[10,20,30,40],"K2":[100,200,300,400]})
st.write("sample data frame from pandas")
# dispaly the dataframe
st.write(df)

df1 = pd.DataFrame(np.random.randn(20,3),columns=['A','B','C'])
#st.line_chart(df1)


