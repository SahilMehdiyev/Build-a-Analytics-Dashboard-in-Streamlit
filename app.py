import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import altair as alt
import pandas as pd
import requests

# endpoints
swapi_endpoint = 'https://swapi.dev/api/people/1/'
api_url = 'http://127.0.0.1:8000/api/customers/'


def fetch_data(endpoint):
    response = requests.get(endpoint)
    data = response.json()
    return data


def send_data(name,gender,age,favorite_number):
    gender_value = '0' if gender == 'Female' else '1'
    data = {
        'name': name,
        'gender': gender_value,
        'age': age,
        'favorite_number': favorite_number
    }
    response = requests.post(api_url, json=data)
    return response


st.title('Analytics Dashboard')
st.write('v.0.0.1')


# Layout customization
col1, col2 = st.columns(2)

with col1:
    st.header('Column 1')
    st.write('some content')
    
    with st.expander('Click to choose something'):
        st.write('option to choose')
        st.write('Another option to choose')

with col2:
    # st.header('Column 2')
    # test chart
    categories = ['A','B','C','D']
    values = np.random.randint(10,100,size=(4,))


    fig, ax = plt.subplots()
    ax.bar(categories, values, color='blue')
    ax.set_xlabel('categories')
    ax.set_ylabel('values')
    ax.set_title('First bar chart')
    st.pyplot(fig)
    

# Session state
if 'counter' not in st.session_state:
    st.session_state.counter = 0
    
# increment btn
if st.button('increment'):
    st.session_state.counter += 1
    

st.write(f'Counter value: {st.session_state.counter}')


# data from SWAPI API
swapi_data = fetch_data(swapi_endpoint)

st.write('Data from the SWAPI API')
st.json(swapi_data)

# Fetch data from our API
data = fetch_data(api_url)

if data:
    df = pd.DataFrame(data)
    
    st.dataframe(df) 
    
    scatter_chart = alt.Chart(df).mark_circle().encode(
        x='age',
        y='favorite_number'
    )
    
    st.altair_chart(scatter_chart, use_container_width=True)
    

name = st.text_input('Your name')
gender = st.radio('Select your gender', ['Male','Female'])
age = st.slider('Select your age', 1, 100, 18)
favorite_number = st.number_input('Enter your favorite number', step=1)

if st.button('Submit'):
    response = send_data(name,gender,age,favorite_number)
    if response.status_code == 201:
        st.success('New customer data created')
    else:
        st.error('Something went wrong')