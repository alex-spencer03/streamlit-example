from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

# configuring page settings
st.set_page_config(page_title='My first app', page_icon=':shark:', layout = 'wide')


st.title('Cost Estimation App')

st.markdown('## Welcome!')
st.markdown('Please begin by filling in the sidebar fields. Your preferred procurement and tendering routes will then be compared in the below bar charts')

st.sidebar.markdown('# Project and Preferences')


col1, col2 = st.columns((1,1))



with col1:
  st.subheader('Your Procurement Route')

  
  
with col2:
  st.subheader('Your Tenderings Route')

  
  
  
  
