import streamlit as st
import pandas as pd
import numpy as np 
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


# loading data in for app 
df_2000 = pd.read_csv('datasets\per_capita_2000.csv')
df_2001 = pd.read_csv('datasets\per_capita_2001.csv')
df_2002 = pd.read_csv('datasets\per_capita_2002.csv')
df_2003 = pd.read_csv('datasets\per_capita_2003.csv')
df_2004 = pd.read_csv('datasets\per_capita_2004.csv')
df_2005 = pd.read_csv('datasets\per_capita_2005.csv')
df_2006 = pd.read_csv('datasets\per_capita_2006.csv')
df_2007 = pd.read_csv('datasets\per_capita_2007.csv')
df_2008 = pd.read_csv('datasets\per_capita_2008.csv')
df_2009 = pd.read_csv('datasets\per_capita_2009.csv')
df_2010 = pd.read_csv('datasets\per_capita_2010.csv')
df_2011 = pd.read_csv('datasets\per_capita_2011.csv')
df_2012 = pd.read_csv('datasets\per_capita_2012.csv')
df_2013 = pd.read_csv('datasets\per_capita_2013.csv')
df_2014 = pd.read_csv('datasets\per_capita_2014.csv')
df_2015 = pd.read_csv('datasets\per_capita_2015.csv')
df_2016 = pd.read_csv('datasets\per_capita_2016.csv')
df_2017 = pd.read_csv('datasets\per_capita_2017.csv')
df_2018 = pd.read_csv('datasets\per_capita_2018.csv')
df_2019 = pd.read_csv('datasets\per_capita_2019.csv')
df_2020 = pd.read_csv('datasets\per_capita_2020.csv')

# prep data for map visualizations

state_dict = {'Alabama':'AL','Alaska':'AK','Arizona':'AZ','Arkansas':'AR','California':'CA','Colorado':'CO','Connecticut':'CT','Delaware':'DE','District of Columbia':'DC','Florida':'FL','Georgia':'GA','Idaho':'ID', 'Illinois':'IL','Indiana':'IN', 'Iowa':'IA','Kansas':'KS', 'Kentucky':'KY', 'Louisiana':'LA', 'Maine':'ME', 'Maryland':'MD','Massachusetts':'MA', 'Michigan':'MI', 'Minnesota':'MN', 'Mississippi':'MS', 'Missouri':'MO', 'Montana':'MT', 'Nebraska':'NE', 'Nevada':'NV', 'New Hampshire':'NH', 'New Jersey':'NJ', 'New Mexico':'NM', 'New York':'NY', 'North Carolina':'NC', 'North Dakota':'ND', 'Ohio':'OH','Oklahoma':'OK', 'Oregon':'OR','Pennsylvania':'PA', 'Rhode Island':'RI', 'South Carolina':'SC', 'South Dakota':'SD', 'Tennessee':'TN', 'Texas':'TX', 'Utah':'UT', 'Vermont':'VT', 'Virginia':'VA', 'Washington':'WA', 'West Virginia':'WV', 'Wisconsin':'WI', 'Wyoming':'WY'}

map_2000 = df_2000.copy()
map_2000.drop(index=[8], inplace=True)
map_2000.replace(state_dict, inplace=True)
map_2000.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2000 = px.choropleth(map_2000, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "tempo",
                         height=500,
                         width=750)
fig_2000.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2000')

map_2001 = df_2001.copy()
map_2001.drop(index=[8], inplace=True)
map_2001.replace(state_dict, inplace=True)
map_2001.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2001 = px.choropleth(map_2001, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "tempo")
fig_2001.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2001')

map_2002 = df_2002.copy()
map_2002.drop(index=[8], inplace=True)
map_2002.replace(state_dict, inplace=True)
map_2002.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2002 = px.choropleth(map_2002, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "tempo")
fig_2002.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2002')

map_2003 = df_2003.copy()
map_2003.drop(index=[8], inplace=True)
map_2003.replace(state_dict, inplace=True)
map_2003.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2003 = px.choropleth(map_2003, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "tempo")
fig_2003.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2003')

map_2004 = df_2004.copy()
map_2004.drop(index=[8], inplace=True)
map_2004.replace(state_dict, inplace=True)
map_2004.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2004 = px.choropleth(map_2004, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "tempo")
fig_2004.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2004')

map_2005 = df_2005.copy()
map_2005.drop(index=[8], inplace=True)
map_2005.replace(state_dict, inplace=True)
map_2005.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2005 = px.choropleth(map_2005, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "tempo")
fig_2005.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2005')

map_2006 = df_2006.copy()
map_2006.drop(index=[8], inplace=True)
map_2006.replace(state_dict, inplace=True)
map_2006.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2006 = px.choropleth(map_2006, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "tempo")
fig_2006.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2006')

map_2007 = df_2007.copy()
map_2007.drop(index=[8], inplace=True)
map_2007.replace(state_dict, inplace=True)
map_2007.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2007 = px.choropleth(map_2007, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "tempo")
fig_2007.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2007')

map_2008 = df_2008.copy()
map_2008.drop(index=[8], inplace=True)
map_2008.replace(state_dict, inplace=True)
map_2008.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2008 = px.choropleth(map_2008, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "tempo")
fig_2008.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2008')

map_2009 = df_2009.copy()
map_2009.drop(index=[8], inplace=True)
map_2009.replace(state_dict, inplace=True)
map_2009.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2009 = px.choropleth(map_2009, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "tempo")
fig_2009.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2009')

map_2010 = df_2010.copy()
map_2010.drop(index=[8], inplace=True)
map_2010.replace(state_dict, inplace=True)
map_2010.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2010 = px.choropleth(map_2010, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "tempo")
fig_2010.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2010')

map_2011 = df_2011.copy()
map_2011.drop(index=[8], inplace=True)
map_2011.replace(state_dict, inplace=True)
map_2011.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2011 = px.choropleth(map_2011, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "tempo")
fig_2011.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2011')

map_2012 = df_2012.copy()
map_2012.drop(index=[8], inplace=True)
map_2012.replace(state_dict, inplace=True)
map_2012.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2012 = px.choropleth(map_2012, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "tempo")
fig_2012.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2012')

map_2013 = df_2013.copy()
map_2013.drop(index=[8], inplace=True)
map_2013.replace(state_dict, inplace=True)
map_2013.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2013 = px.choropleth(map_2013, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "tempo")
fig_2013.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2013')

map_2014 = df_2014.copy()
map_2014.drop(index=[8], inplace=True)
map_2014.replace(state_dict, inplace=True)
map_2014.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2014 = px.choropleth(map_2014, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "tempo")
fig_2014.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2014')

map_2015 = df_2015.copy()
map_2015.drop(index=[8], inplace=True)
map_2015.replace(state_dict, inplace=True)
map_2015.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2015 = px.choropleth(map_2015, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "tempo")
fig_2015.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2015')

map_2016 = df_2016.copy()
map_2016.drop(index=[8], inplace=True)
map_2016.replace(state_dict, inplace=True)
map_2016.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2016 = px.choropleth(map_2016, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "tempo")
fig_2016.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2016')

map_2017 = df_2017.copy()
map_2017.drop(index=[8], inplace=True)
map_2017.replace(state_dict, inplace=True)
map_2017.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2017 = px.choropleth(map_2017, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "tempo")
fig_2017.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2017')

map_2018 = df_2018.copy()
map_2018.drop(index=[8], inplace=True)
map_2018.replace(state_dict, inplace=True)
map_2018.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2018 = px.choropleth(map_2018, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "tempo")
fig_2018.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2018')

map_2019 = df_2019.copy()
map_2019.drop(index=[8], inplace=True)
map_2019.replace(state_dict, inplace=True)
map_2019.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2019 = px.choropleth(map_2019, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "tempo")
fig_2019.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2019')

map_2020 = df_2020.copy()
map_2020.drop(index=[8], inplace=True)
map_2020.replace(state_dict, inplace=True)
map_2020.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2020 = px.choropleth(map_2020, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "tempo")
fig_2020.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2020')

# prep data for state histograms 

df_state_pc_totals = pd.read_csv('datasets\state_totals_by_year.csv')











# streamlit front end view


# main title
st.title("U.S. Hate Crimes from 2000-2020") 

# histograms by state

st.subheader("Trend in Hate Crimes Per Capita By State 2000-2020")

st.line_chart(data=df_state_pc_totals['Alabama'])









#map visuals

st.subheader('U.S. Map Density Chart')
year = st.slider('Move slider to see data from each year', 2000, 2020, 2000)
    
if year == 2000:
    st.plotly_chart(fig_2000)
if year == 2001:    
    st.plotly_chart(fig_2001)
if year == 2002:
    st.plotly_chart(fig_2002)
if year == 2003:    
    st.plotly_chart(fig_2003)
if year == 2004:
    st.plotly_chart(fig_2004)
if year == 2005:    
    st.plotly_chart(fig_2005)
if year == 2006:
    st.plotly_chart(fig_2006)
if year == 2007:    
    st.plotly_chart(fig_2007)
if year == 2008:    
    st.plotly_chart(fig_2008)
if year == 2009:    
    st.plotly_chart(fig_2009)
if year == 2010:    
    st.plotly_chart(fig_2010)
if year == 2011:    
    st.plotly_chart(fig_2011)
if year == 2012:    
    st.plotly_chart(fig_2012)
if year == 2013:    
    st.plotly_chart(fig_2013)
if year == 2014:    
    st.plotly_chart(fig_2014)
if year == 2015:    
    st.plotly_chart(fig_2015)
if year == 2016:    
    st.plotly_chart(fig_2016)
if year == 2017:    
    st.plotly_chart(fig_2017)
if year == 2018:    
    st.plotly_chart(fig_2018)
if year == 2019:    
    st.plotly_chart(fig_2019)
if year == 2020:    
    st.plotly_chart(fig_2020)

# Raw data section

st.subheader('See raw data')
st.caption('See raw data for total incidents per year per state (per 100,000 people)')
st.caption('(Hint: Once the dataset is selected, click the column name to sort by ascending or descending values)')
with st.expander('click to choose dataset'):
    if st.checkbox('2000'):
        st.write(df_2000[['state', 'total_incidents_per_capita']])
    if st.checkbox('2001'):
        st.write(df_2001[['state', 'total_incidents_per_capita']])
    if st.checkbox('2002'):
        st.write(df_2002[['state', 'total_incidents_per_capita']])
    if st.checkbox('2003'):
        st.write(df_2003[['state', 'total_incidents_per_capita']])
    if st.checkbox('2004'):
        st.write(df_2004[['state', 'total_incidents_per_capita']])
    if st.checkbox('2005'):
        st.write(df_2005[['state', 'total_incidents_per_capita']])
    if st.checkbox('2006'):
        st.write(df_2006[['state', 'total_incidents_per_capita']])
    if st.checkbox('2007'):
        st.write(df_2007[['state', 'total_incidents_per_capita']])
    if st.checkbox('2008'):
        st.write(df_2008[['state', 'total_incidents_per_capita']])
    if st.checkbox('2009'):
        st.write(df_2009[['state', 'total_incidents_per_capita']])
    if st.checkbox('2010'):
        st.write(df_2010[['state', 'total_incidents_per_capita']])
    if st.checkbox('2011'):
        st.write(df_2011[['state', 'total_incidents_per_capita']])
    if st.checkbox('2012'):
        st.write(df_2013[['state', 'total_incidents_per_capita']])
    if st.checkbox('2014'):
        st.write(df_2014[['state', 'total_incidents_per_capita']])
    if st.checkbox('2015'):
        st.write(df_2015[['state', 'total_incidents_per_capita']])
    if st.checkbox('2016'):
        st.write(df_2016[['state', 'total_incidents_per_capita']])
    if st.checkbox('2017'):
        st.write(df_2017[['state', 'total_incidents_per_capita']])
    if st.checkbox('2018'):
        st.write(df_2018[['state', 'total_incidents_per_capita']])
    if st.checkbox('2019'):
        st.write(df_2019[['state', 'total_incidents_per_capita']])
    if st.checkbox('2020'):
        st.write(df_2020[['state', 'total_incidents_per_capita']])
