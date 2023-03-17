import streamlit as st
import pickle

pickle.dump(model, open(filename, "wb"))
model = pickle.load(open(filename, "rb"))
st.title('REVENUE PREDICTION')
tem = st.number_input('Input Temperature')
if st.button('Predict'):
  result = model.predict(tem)
  st.success(f'{result}')
