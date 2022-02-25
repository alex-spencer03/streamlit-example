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
with st.form("my_form"):
    st.write("Section 1")
    name = st.text_input('1. Your name','')
    company = st.text_input('2. Your company','')
    profession = st.radio('3. Profession',('Quantity Surveyor','Architect','Project Manager', 'Client', 'Designer', 'Other'))
    project_name = st.text_input('4. Project name','')
    riba_stages = st.radio('5. RIBA Stages', ('Stage 0-1 Strategic Definition + Feasibility', 'Stage 2-4 Concept, Developed and Technical Design',\
                                              'Stage 5-6 Construction + Handover', 'Stage 7 In Use'))
    start_date = st.date_input('6. Start date on site', datetime.date(2022,3,1))

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")





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


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
