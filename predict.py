import streamlit as st
import numpy as np
import pickle

filename = 'model.pickle'

model = pickle.load(open(filename, "rb"))
st.title('REVENUE PREDICTION')
tem = st.number_input('Input Temperature')
tem = np.array(tem).reshape(-1,1)
if st.button('Predict'):
  result = model.predict(tem)
  st.success(f'{result}')
