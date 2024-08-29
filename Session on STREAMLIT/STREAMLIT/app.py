import streamlit as st
import pandas as pd
import time

# streamlit docs: https://docs.streamlit.io/develop/api-reference

# All the elements are called widgets.
# to run: streamlit run filename
# 'locathost' same as 127.0.0.1

# Text Utilities
st.title('Text Utilities')
st.header('I am learning Streamlit')
st.subheader('Lets see if I love it!')
st.write('This is a normal text.')
st.markdown('''
            ### This is a markdown
            - number 1
            - number 2
            - number 3
           ''')
# learn about markdown: https://www.markdownguide.org/basic-syntax/#images-1

st.code('''
        def square(input):
            return input**2
        
        square(2)
''')

st.latex('x^2 + y^2 + 2 = 0')
# https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes#What_is_LaTeX.3F
# Used for math symbols.


# Display elements
st.title('Display elements')

# 1. DataFrame
df = pd.DataFrame({
    'name': ['A', 'B', 'C'],
    'marks': [70,80,90],
    'package': [20,10,15]
})
st.dataframe(df)

# 2. metric
st.metric('revenue', '₹ 3L', '3%')
st.metric('revenue', '₹ 3L', '-3%')

# 3. json
st.json({
    'name': ['A', 'B', 'C'],
    'marks': [70,80,90],
    'package': [20,10,15]
})


# Display media
st.title('Display media')
st.image('resources/1.jpg')

st.video('resources/6013748_Nature_Misty_1280x720.mp4')

st.audio('resources/nature-birds-singing-217212.mp3')


# Creating layouts
st.sidebar.title('Sidebar ka title')

col1, col2, col3 = st.columns(3)
with col1:
    st.image('resources/2.jpg')
with col2:
    st.image('resources/3.jpg')
with col3:
    st.image('resources/4.jpg')


# Showing status
st.success('Login success!')
st.error('Login failed!')
st.info('An information.')
st.warning('A warning!')

bar = st.progress(0)
for i in range(1, 101):
    # time.sleep(0.01)
    bar.progress(i)


# Taking user input
name = st.text_input('Enter name')
age = st.number_input('Enter age')
st.date_input('Enter dob')


# file upload
file = st.file_uploader('Upload a CSV file')

if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())

