import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title('Analytics Dashboard')
st.write('v.0.0.1')


# Layout customization
col1, col2 = st.columns(2)

with col1:
    st.header('Column 1')

with col2:
    st.header('Column 2')
    


# test chart
categories = ['A','B','C','D']
values = np.random.randint(10,100,size=(4,))


fig, ax = plt.subplots()
ax.bar(categories, values, color='blue')
ax.set_xlabel('categories')
ax.set_ylabel('values')
ax.set_title('First bar chart')
st.pyplot(fig)