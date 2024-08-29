import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title='Startup Analysis')

df = pd.read_csv('analysis\startup_cleaned.csv')

# df['year'] = df['year'].astype('datetime')

def load_investor_details(investor):
    st.title(investor)
    # load the recent 5 investments of the investor
    recent5_df = df[df['investors'].str.contains(investor)].head()[['date','startup','vertical','city','round','amount']]
    st.subheader('Most recent investments')
    st.dataframe(recent5_df)

    col1, col2 = st.columns(2)
    # biggest investments
    with col1:
        biggest_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        st.subheader('Biggest Investments')
        st.dataframe(biggest_series)

    with col2:
        fig, ax = plt.subplots()
        ax.bar(biggest_series.index, biggest_series.values)

        st.pyplot(fig)
    
    st.subheader('Sectors invested in...')
    vertical_series = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
    fig1, ax1 = plt.subplots()
    ax1.pie(vertical_series, labels=vertical_series.index, autopct='%0.01f%%')

    st.pyplot(fig1)

    st.subheader('Round')
    round_series = df[df['investors'].str.contains(investor)].groupby('round')['amount'].sum()
    fig2, ax2 = plt.subplots()
    ax2.pie(round_series, labels=round_series.index, autopct='%0.01f%%')

    st.pyplot(fig2)

    st.subheader('City')
    city_series = df[df['investors'].str.contains(investor)].groupby('city')['amount'].sum()
    fig3, ax3 = plt.subplots()
    ax3.pie(city_series, labels=city_series.index, autopct='%0.01f%%')

    st.pyplot(fig3)

    st.subheader('YoY investment')
    yr_series = df[df['investors'].str.contains(' IDG Ventures')].groupby('year')['amount'].sum()
    fig4, ax4 = plt.subplots()
    ax4.line(yr_series.index, yr_series.values)

    st.pyplot(fig4)


def load_overall_analysis():
    st.title('Overall analsysis') 

# st.dataframe(df)

st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select One', ['Overall Analysis','Startup','Investor'])

if option == 'Overall Analysis':
    st.title('Overall Analysis')
    btn0 = st.sidebar.button('Show overall analysis')

    if btn0:
        load_overall_analysis()

elif option == 'Startup':
    st.title('Startup Analysis')
    st.sidebar.selectbox('Select Startup',sorted(list(df['startup'].unique())))
    btn1 = st.sidebar.button('Find Startup details')

else:
    # st.title('Investor Analysis')
    selected_investor = st.sidebar.selectbox('Select Investor',sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor details')

    if btn2:
        load_investor_details(selected_investor)
        


















