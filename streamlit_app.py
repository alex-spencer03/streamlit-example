from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

# configuring page settings
st.set_page_config(page_title='My first app', page_icon=':shark:', layout = 'wide')


st.title('Cost Estimation App')

st.markdown('## Project Information')

col1, col2 = st.columns((1,1))

with col1:
  st.selectbox('What is the location?', ('London', 'Nottingham', 'Edinburgh'))
  st.selectbox('What is the tendering strategy?', ('Single', 'Double'))
  st.selectbox('What BREEAM rating would you like?', ('Oustanding', 'Very Good'))


with col2:
  st.selectbox('What is the base date?', ('Q2 2022', 'Q3 2022'))
  st.selectbox('What is the contract type?', ('Option1', 'Option2'))
  st.selectbox('What WELL rating would you like?',('Oustanding', 'Very Good'))
  

  
st.sidebar.markdown('# Project and Preferences')



  
  
