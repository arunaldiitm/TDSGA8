import streamlit as st

st.header('enter two mumber')

def user_input():
    first_no = st.number_input("first_no", min_value = 0.0, max_value = 100000000000.0)
    second_no = st.number_input("second_no", min_value = 0.0, max_value = 100000000000.0)
