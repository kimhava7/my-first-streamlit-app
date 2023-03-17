import streamlit as st
import pickle

filename = 'model.pickle'

model = pickle.load(open('model.pickle', "rb"))
st.title('REVENUE PREDICTION')
tem = st.number_input('Input Temperature')
if st.button('Predict'):
  result = model.predict(tem)
  st.success(f'{result}')
