import streamlit as st

st.markdown("### :blue[Visualizing 'Brexit Regret']")

col_main1, col_main2 = st.columns((3,1))
with col_main1:

    st.write("__Which way would you vote if there were another Brexit referendum?__")

    st.write("""We are going to look at the results of a poll that asked 'Which way would you vote if there were another EU referendum'. 
    This should be viewed in conjunction with the article on [Medium]().
    The data used here is a subset of the data derived from the polling data referred to in the article.""")
    st.write("__Select one of the tabs below for the results:__")

with col_main2:
        st.image('poll/guillaume-perigois-0NRkVddA2fw-unsplash.jpg')
        st.caption('Photo by Guillaume Périgois on Unsplash')

tab_result, tab_regions, tab_age, tab_data = st.tabs(['Overall result','Regional result','Result by age', 'Data tables'])

import overall
overall.overall(tab_result)

import regions
regions.regions(tab_regions)

import age
age.age(tab_age)

import tables
tables.data_tables(tab_data)

