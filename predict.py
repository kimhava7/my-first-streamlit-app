import streamlit as st
import pickle
st.title('REVENUE PREDICTION')
tem = st.number_input('Input Temperature')
if st.button('Predict'):
  model = pickle.load(open(filename, "rb"))
  result = model_selection(tem)
  st.success(f'{result}')
