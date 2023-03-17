import streamlit as st
import pickle
with open('model.pickle', 'rb') as file:
    model = pickle.load(file)
st.title('REVENUE PREDICTION')
tem = st.number_input('Input Temperature')
if st.button('Predict'):
  result = model.predict(tem)
  st.success(f'{result}')
