import streamlit as st
import pandas as pd

st.title("Welcome to streamlit")

#name = st.text_input("Enter your name:")
#st.write(f"Hello {name}")

name = st.text_input("Enter your name:")
age = st.slider("Select your age:",15,100,25)
if name:
    #st.write(f"Hello {name}")
    st.write(f"Hello{name} your age is:{age}")


data = {}
data['Name']=['Ram','Tom','Leo']
data['Dept']=['sales','HR','QA']
data['City']=['City1','City2','City3']

df = st.selectbox("Choose your data:",data)
df = pd.DataFrame(data)
st.write(df)

uploaded_file = st.file_uploader("Choose your input file:",type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)






