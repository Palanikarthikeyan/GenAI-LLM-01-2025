import streamlit as st

st.checkbox('Yes')
st.button('Click Me')
st.radio('Select your option:',['Yes','No'])

st.selectbox('Select your model:',['model1','model2','model3'])
st.multiselect('Choose a planet:',['Jupiter','Mars','Neptune'])

st.slider('Pick a number:',0,100)
st.select_slider('Pick a mark:',['Bad','Good','Excellent'])
