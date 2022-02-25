from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

# configuring page settings
st.set_page_config(page_title='My first app', page_icon=':shark:', layout = 'wide')



st.title('Procurement & Tendering App')

add_selectbox = st.sidebar.write('Welcome!')
add_slider = st.sidebar.write('Please start by inputting your details and project information. Press submit to generate your options.')


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
    the same as what was agreed at Contract Stage. For example, if you have no contingency at Contract Stage then achieving this price will be of high importance.')
    
    programme_certainty = st.slider('Programme/ Schedule Certainty', min_value = 1, max_value = 3, help='Programme / Schedule refers to the importance of meeting \
    the deadline agreed at Contract Stage. For example, if you are working on a school that needs to be ready on the first day of term then this will be of high importance.')
    
    quality = st.slider('Quality', min_value = 1, max_value = 3, help = 'Quality refers to the importance of achieving a specific tolerance level. For example, \
    if you are working on a 5* hotel development then meeting the the quality level and tight tolerance desired by the customer is of high importance.')
    
    sr.write('16. Statements')
    st.write('Please rate the following on a 0 to 5 scale, 1 being the least important and 5 being the most important. Please see below some project examples that \
    may apply for each of the statements:\
    0 - not applicable\
    1 - very low importance - for Provisional Sums Left in the Contract, you are accepting of having a large portion of the Contract Value (>10%) as Provisional Sums.\
    3 -  medium importance - for Contractor Involvement During Design, you are accepting in giving the Contractor design responsibility for some elements of the scheme \
    (waterproofing, structural adaptions etc.).\
    5 - very high importance - for Programme Certainty, you are a school that has to be open for term time on 1st September and there is no Plan B if the project is delayed.')




left_column, right_column = st.columns(2)
left_column.button('Press me darling!')

with right_column:
    chosen = st.radio('Sorting hat',
                      ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")




ff = st.slider('Slider test')
st.write(ff, 'squared is', ff*ff)



