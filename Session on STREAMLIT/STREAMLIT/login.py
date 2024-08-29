import streamlit as st

email = st.text_input('Enter email')
password = st.text_input('Enter password')
gender = st.selectbox('Select gender', ['male','female','others'])

btn = st.button('Login')

# if button is clicked
if btn:
    if email == 'kohlikay879@gmail.com' and password == '123':
        st.success('Login successful!')
        st.balloons()
        st.write(gender)
    else:
        st.error('Login failed!')












