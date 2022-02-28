from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

# configuring page settings
st.set_page_config(page_title='My first app', page_icon=':shark:', layout = 'wide')


st.title('Procurement & Tendering App')

st.markdown('## Welcome!')
st.markdown('Please begin by filling in the sidebar fields. Your preferred procurement and tendering routes will then be compared in the below bar charts')

st.sidebar.markdown('# Project and Preferences')
st.sidebar.text_input('1. Your name','')
st.sidebar.text_input('2. Your company','')
st.sidebar.selectbox('3. Profession',('Quantity Surveyor','Architect','Project Manager', 'Client', 'Designer', 'Other'))
st.sidebar.text_input('4. Project name','')
st.sidebar.selectbox('5. RIBA Stages', ('Stage 0-1 Strategic Definition + Feasibility', 'Stage 2-4 Concept, Developed and Technical Design',\
                                        'Stage 5-6 Construction + Handover', 'Stage 7 In Use'))
st.sidebar.date_input('6. Start date on site')
st.sidebar.date_input('7. Completion date')
st.sidebar.text_input('8. Client name', '')
st.sidebar.radio('9. Client type', ('Private', 'Public'))
st.sidebar.selectbox('10. Sector', ('Residential', 'Hotel', 'Primary and nursery education', 'Secondary education', 'Higher education', 'Commercial offices',\
                                    'Corporate workspace', 'Healthcare', 'Government', 'Defense', 'Aviation', 'Life sciences/ Pharmaceuticals',\
                                    'Industrial and logistics', 'Other'))
st.sidebar.selectbox('11. Build type', ('New Build or New Build behind Retained Facade', 'Extension', 'Light Refurb (finishes only)', 'Medium Refurb (finishes + M&E)',\
                                         'Heavy Refurb (finishes + M&E + structural)', 'New Build + Extension / Refurb'))
st.sidebar.selectbox('12. Project value', ('< £1m', '£1m - £50m', '£50m - £100m', '£100m >'))

preferred_proc_route = st.sidebar.radio('13. What is your preferred procurement route?', ('Design and Build', 'Traditional', 'Management'))
preferred_tend_route = st.sidebar.radio('14. What is your preferred tendering route?', ('Single Stage', 'Two Stage', 'Negotiated'))

st.sidebar.write('15. Please rank the following in terms of importance with 1 being the most important and 3 being the least important.')

cost_certainty = st.sidebar.slider('Cost Certainty',min_value=1, max_value=3, help='Cost Certainty refers to the importance of the Final Account price paid being \
the same as what was agreed at Contract Stage. For example, if you have no contingency at Contract Stage then achieving this price will be of high importance.')

programme_certainty = st.sidebar.slider('Programme/ Schedule Certainty', min_value = 1, max_value = 3, help='Programme / Schedule refers to the importance of meeting \
the deadline agreed at Contract Stage. For example, if you are working on a school that needs to be ready on the first day of term then this will be of high importance.')

quality = st.sidebar.slider('Quality', min_value = 1, max_value = 3, help = 'Quality refers to the importance of achieving a specific tolerance level. For example, \
if you are working on a 5* hotel development then meeting the the quality level and tight tolerance desired by the customer is of high importance.')


st.sidebar.write('16. Statements')
st.sidebar.write('Please rate the following on a 0 to 5 scale, 1 being the least important and 5 being the most important. Please see below some project examples that \
may apply for each of the statements:')

st.sidebar.caption('* 0 - not applicable')
st.sidebar.caption('* 1 - very low importance - for Provisional Sums Left in the Contract, you are accepting of having a large portion of the Contract Value (>10%)\
as Provisional Sums.')
st.sidebar.caption('* 3 -  medium importance - for Contractor Involvement During Design, you are accepting in giving the Contractor design responsibility for some \
elements of the scheme (waterproofing, structural adaptions etc.)')
st.sidebar.caption('* 5 - very high importance - for Programme Certainty, you are a school that has to be open for term time on 1st September and there is no Plan B\
if the project is delayed.')


risk_transfer = st.sidebar.slider('Risk transfer to the Contractor', min_value = 0, max_value = 5)
overlapping = st.sidebar.slider('Overlapping design and construction', min_value = 0, max_value = 5)
contractor_involvement = st.sidebar.slider('Contractor Involvement in Design', min_value = 0, max_value = 5)
provisional_sums = st.sidebar.slider('Provisional Sums left in the Contract', min_value = 0, max_value = 5)
market_competition = st.sidebar.slider('Market Competition when Tendering', min_value = 0, max_value = 5)
contractor_incentive = st.sidebar.slider('Contractor Incentives for Risk Mitigation', min_value = 0, max_value = 5)
competition_regulations = st.sidebar.slider('Compliance with competition regulations(public body)', min_value = 0, max_value = 5)



col1, col2 = st.columns((1,1))


    
######## CALCULATIONS ###########

#### GROUP: Scot, Schedule & Quality

# user input test values
#cost_certainty = 2
#programme_certainty = 1
#quality = 3

################################################ DF details
# setting df with calculations and user input
first_cols1 = {'Question':['Price', 'Programme', 'Quality'], 'Score':[cost_certainty, programme_certainty, quality]}

# to dataframe
df_calcs1 = pd.DataFrame(first_cols1)

# adding group set values as columns
df_calcs1['Max'] = 3
df_calcs1['Group_var'] = 60


############################# First calculation
total_score_sum1 = df_calcs1['Score'].sum()
df_calcs1['Calc1'] = df_calcs1['Score']/total_score_sum1*100

# rounding to whole numbers
df_calcs1['Calc1'] = np.round(df_calcs1['Calc1'], decimals = 0)


########################### Results calculations
total_calcs1 = df_calcs1['Calc1'].sum()
df_calcs1['Result_factor'] = df_calcs1['Calc1']/total_calcs1*df_calcs1['Group_var']

# rounding to whole numbers
df_calcs1['Result_factor'] = np.round(df_calcs1['Result_factor'], decimals = 0)


################################################ DF details
first_cols2 = {'Question':['Risk', 'Overlapping', 'Contractor involvement', 'Provisional sums', 'Competition', 'Incentive',\
                          'Competition regulations'],\
               'Score':[risk_transfer, overlapping, contractor_involvement, provisional_sums, market_competition,\
                       contractor_incentive, competition_regulations]}

# to dataframe
df_calcs2 = pd.DataFrame(first_cols2)

# adding group set values as new columns
df_calcs2['Max'] = 5
df_calcs2['Group_var'] = 40

############################# First calculation
df_calcs2['Calc1'] = (df_calcs2['Score']/df_calcs2['Max'])/7*100

# converting to int
#df_calcs2['Calc1'] = df_calcs2['Calc1'].apply(pd.to_numeric)

#rounding up
df_calcs2['Calc1'] = np.round(df_calcs2['Calc1'], decimals = 0)

########################### Results calculations
total_calcs2 = df_calcs2['Calc1'].sum()

df_calcs2['Result_factor'] = df_calcs2['Calc1']/total_calcs2*df_calcs2['Group_var']

# converting to int
#df_calcs2['Result_factor'] = df_calcs2['Result_factor'].apply(pd.to_numeric)

#rounding up
df_calcs2['Result_factor'] = np.round(df_calcs2['Result_factor'], decimals = 0)



# combining into one df
master = df_calcs1.append(df_calcs2, ignore_index=True)



# setting df with set values and user inputs
data = {'Question':['Price', 'Programme', 'Quality', 'Risk', 'Overlapping', 'Contractor involvement', 'Provisional sums', 'Competition', 'Incentive',\
                    'Competition regulations'],\
        'Proc_Design':[0.33,0.5,0.33,0.5,0.33,0.5,0.5,0.33,0.5,0.38],\
        'Proc_Traditional':[0.5,0.33,0.5,0.33,0.17,0.17,0.33,0.5,0.33,0.38],\
        'Proc_Management':[0.17,0.17,0.17,0.17,0.5,0.33,0.17,0.17,0.17,0.25],\
        'Tendering_Single':[0.33, 0.29, 0.50, 0.38,	0.25, 0.17,	0.33, 0.50, 0.25, 0.38],\
        'Tendering_Two':[0.33, 0.43, 0.33, 0.38, 0.38, 0.50, 0.33, 0.33, 0.38, 0.38],\
        'Tendering_Negotiated':[0.33, 0.29, 0.17, 0.25, 0.38, 0.33, 0.33, 0.17, 0.38, 0.25]
       }

df_fixed_values = pd.DataFrame(data)


# new df with procurement preferences
df_proc_preferences = pd.DataFrame()

# new columns calculating the scores
df_proc_preferences['Design and Build'] = df_fixed_values['Proc_Design'] * master['Result_factor']
df_proc_preferences['Traditional'] = df_fixed_values['Proc_Traditional'] * master['Result_factor']
df_proc_preferences['Management'] = df_fixed_values['Proc_Management']  * master['Result_factor']

df_proc_preferences = df_proc_preferences.round(0)

# summing all values in all columns
final_proc = df_proc_preferences.sum(axis=0)
final_proc = pd.DataFrame(final_proc)
final_proc.reset_index()

###############################################################

# new df with tendering preferences

df_tend_preferences = pd.DataFrame()

# new columns calculating scores
df_tend_preferences['Single Stage'] = df_fixed_values['Tendering_Single']  * master['Result_factor']
df_tend_preferences['Two Stage'] = df_fixed_values['Tendering_Two']  * master['Result_factor']
df_tend_preferences['Negotiated'] = df_fixed_values['Tendering_Negotiated']  * master['Result_factor']

df_tend_preferences = df_tend_preferences.round(0)

# summing all values in all columns
final_tend = df_tend_preferences.sum(axis=0)
final_tend = pd.DataFrame(final_tend)
final_tend.reset_index()



with col1:
 st.bar_chart(final_proc, height = 100)

 with col2:
  st.bar_chart(final_tend)
  
  
  
  
