from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

# configuring page settings
st.set_page_config(page_title='My first app', page_icon=':shark:', layout = 'wide')


st.title('Procurement & Tendering App')

add_selectbox = st.sidebar.markdown('# Welcome!')

col1, col2, col3, col4 = st.columns((1,1,1,1))

with col1:
    with st.expander('About You'):
        st.text_input('1. Your name','')
        st.text_input('2. Your company','')
        st.selectbox('3. Profession',('Quantity Surveyor','Architect','Project Manager', 'Client', 'Designer', 'Other'))
   
with col1:
    with st.expander('About Your Project'):
        st.text_input('4. Project name','')
        st.selectbox('5. RIBA Stages', ('Stage 0-1 Strategic Definition + Feasibility', 'Stage 2-4 Concept, Developed and Technical Design',\
                                    'Stage 5-6 Construction + Handover', 'Stage 7 In Use'))
        st.date_input('6. Start date on site')
        st.date_input('7. Completion date')
        st.text_input('8. Client name', '')
        st.radio('9. Client type', ('Private', 'Public'))
        st.selectbox('10. Sector', ('Residential', 'Hotel', 'Primary and nursery education', 'Secondary education', 'Higher education', 'Commercial offices',\
                                'Corporate workspace', 'Healthcare', 'Government', 'Defense', 'Aviation', 'Life sciences/ Pharmaceuticals',\
                                'Industrial and logistics', 'Other'))
        st.selectbox('11. Build type', ('New Build or New Build behind Retained Facade', 'Extension', 'Light Refurb (finishes only)', 'Medium Refurb (finishes + M&E)',\
                                    'Heavy Refurb (finishes + M&E + structural)', 'New Build + Extension / Refurb'))
        st.selectbox('12. Project value', ('< £1m', '£1m - £50m', '£50m - £100m', '£100m >'))


with col1:
    with st.expander('Tendering & Procurement'):
        preferred_proc_route = st.radio('13. What is your preferred procurement route?', ('Design and Build', 'Traditional', 'Management'))
        preferred_tend_route = st.radio('14. What is your preferred tendering route?', ('Single Stage', 'Two Stage', 'Negotiated'))
        
        st.write('15. Please rank the following in terms of importance with 1 being the most important and 3 being the least important.')
        
        cost_certainty = st.slider('Cost Certainty',min_value=1, max_value=3, help='Cost Certainty refers to the importance of the Final Account price paid being \
        the same as what was agreed at Contract Stage. For example, if you have no contingency at Contract Stage then achieving this price will be of high importance.')
        
        programme_certainty = st.slider('Programme/ Schedule Certainty', min_value = 1, max_value = 3, help='Programme / Schedule refers to the importance of meeting \
        the deadline agreed at Contract Stage. For example, if you are working on a school that needs to be ready on the first day of term then this will be of high importance.')
        
        quality = st.slider('Quality', min_value = 1, max_value = 3, help = 'Quality refers to the importance of achieving a specific tolerance level. For example, \
        if you are working on a 5* hotel development then meeting the the quality level and tight tolerance desired by the customer is of high importance.')
        
        st.write('16. Statements')
        st.write('Please rate the following on a 0 to 5 scale, 1 being the least important and 5 being the most important. Please see below some project examples that \
        may apply for each of the statements:')
        
        """
        * 0 - not applicable
        * 1 - very low importance - for Provisional Sums Left in the Contract, you are accepting of having a large portion of the Contract Value (>10%) as Provisional Sums.
        * 3 -  medium importance - for Contractor Involvement During Design, you are accepting in giving the Contractor design responsibility for some elements \
        of the scheme (waterproofing, structural adaptions etc.)
        * 5 - very high importance - for Programme Certainty, you are a school that has to be open for term time on 1st September and there is no Plan B if the \
        #project is delayed.')
        """
        
        st.write('')   
        risk_transfer = st.slider('Risk transfer to the Contractor', min_value = 0, max_value = 5)
        overlapping = st.slider('Overlapping design and construction', min_value = 0, max_value = 5)
        contractor_involvement = st.slider('Contractor Involvement in Design', min_value = 0, max_value = 5)
        provisional_sums = st.slider('Provisional Sums left in the Contract', min_value = 0, max_value = 5)
        market_competition = st.slider('Market Competition when Tendering', min_value = 0, max_value = 5)
        contractor_incentive = st.slider('Contractor Incentives for Risk Mitigation', min_value = 0, max_value = 5)
        competition_regulations = st.slider('Compliance with competition regulations(public body)', min_value = 0, max_value = 5)
       
    
######## CALCULATIONS ###########

# setting df with set values and user inputs
data = {'Question':['Price Certainty', 'Programme', 'Quality', 'Risk Transfer', 'Overlapping', 'Contractor involvement', 'Provisional sums', 'Competition', 'Incentive',\
                    'Competition regulations'],\
       'Score':[cost_certainty, programme_certainty, quality,  risk_transfer, overlapping, contractor_involvement, provisional_sums, market_competition, contractor_incentive,\
               competition_regulations],\
       'Max value':[3,3,3,5,5,5,5,5,5,5],\
       'Global variable':[60,60,60,40,40,40,40,40,40,40],\
       'Proc_Design':[0.33,0.5,0.33,0.5,0.33,0.5,0.5,0.33,0.5,0.38],\
       'Proc_Traditional':[0.5,0.33,0.5,0.33,0.17,0.17,0.33,0.5,0.33,0.38]
       }
#df = pd.DataFrame()




left_column, right_column = st.columns(2)
left_column.button('Press me darling!')

with right_column:
    chosen = st.radio('Sorting hat',
                      ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")




ff = st.slider('Slider test')
st.write(ff, 'squared is', ff*ff)



