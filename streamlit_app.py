from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

# configuring page settings
st.set_page_config(page_title='My first app', page_icon=':shark:', layout = 'wide')



st.title('Procurement & Tendering App')

# form details
#with st.form("my_form"):

with st.expander('Testing'):
    # section 1 questions
    st.write("Section 1")
    name = st.text_input('1. Your name','')
    company = st.text_input('2. Your company','')
    profession = st.radio('3. Profession',('Quantity Surveyor','Architect','Project Manager', 'Client', 'Designer', 'Other'))
    project_name = st.text_input('4. Project name','')
    riba_stages = st.radio('5. RIBA Stages', ('Stage 0-1 Strategic Definition + Feasibility', 'Stage 2-4 Concept, Developed and Technical Design',\
                                              'Stage 5-6 Construction + Handover', 'Stage 7 In Use'))
    start_date = st.date_input('6. Start date on site')
    completion_date = st.date_input('7. Completion date')
    client_name = st.text_input('8. Client name', '')
    client_type = st.radio('9. Client type', ('Private', 'Public'))
    sector = st.radio('10. Sector', ('Residential', 'Hotel', 'Primary and nursery education', 'Secondary education', 'Higher education', 'Commercial offices',\
                                    'Corporate workspace', 'Healthcare', 'Government', 'Defense', 'Aviation', 'Life sciences/ Pharmaceuticals',\
                                    'Industrial and logistics', 'Other'))
    built_type = st.radio('11. Build type', ('New Build or New Build behind Retained Facade', 'Extension', 'Light Refurb (finishes only)', 'Medium Refurb (finishes + M&E)',\
                                            'Heavy Refurb (finishes + M&E + structural)', 'New Build + Extension / Refurb'))
    project_value = st.radio('12. Project value', ('< £1m', '£1m - £50m', '£50m - £100m', '£100m >'))
    preferred_proc_route = st.radio('13. What is your preferred procurement route?', ('Design and Build', 'Traditional', 'Management'))
    preferred_tend_route = st.radio('14. What is your preferred tendering route?', ('Single Stage', 'Two Stage', 'Negotiated'))
    
    
    # section 2 questions
    
with st.expander('Section 2'):
    st.write('15. Please rank the following in terms of importance with 1 being the most important and 3 being the least important.')
    cost_certainty = st.slider('Cost Certainty',min_value=1, max_value=3, help='Cost Certainty refers to the importance of the Final Account price paid being \
    the same as what was agreed at Contract Stage. For example, if you have no contingency at Contract Stage then achieving this price will be of high importance. 
')





add_selectbox = st.sidebar.selectbox('How would you like to be contacted', ('Email','Home phone','Mobile phone'))
add_slider = st.sidebar.slider('Select a range of values', 0.0,100.0,(25.0,75.0))

left_column, right_column = st.columns(2)
left_column.button('Press me darling!')

with right_column:
    chosen = st.radio('Sorting hat',
                      ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")




ff = st.slider('Slider test')
st.write(ff, 'squared is', ff*ff)



