# various imports for data manipulation and visualizations
import streamlit as st
import pandas as pd
import numpy as np 
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt 
from pathlib import Path


# setting up csv paths

csv_2000 = Path("datasets", "per_capita_2000.csv")

# loading data in for app 
df_2000 = pd.read_csv(csv_2000)
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
                         color_continuous_scale = "Reds",
                         height=500,
                         width=750)
fig_2000.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2000')
fig_2000.update_geos(bgcolor='#0E1117')

map_2001 = df_2001.copy()
map_2001.drop(index=[8], inplace=True)
map_2001.replace(state_dict, inplace=True)
map_2001.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2001 = px.choropleth(map_2001, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "Reds")
fig_2001.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2001')
fig_2001.update_geos(bgcolor='#0E1117')

map_2002 = df_2002.copy()
map_2002.drop(index=[8], inplace=True)
map_2002.replace(state_dict, inplace=True)
map_2002.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2002 = px.choropleth(map_2002, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "Reds")
fig_2002.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2002')
fig_2002.update_geos(bgcolor='#0E1117')

map_2003 = df_2003.copy()
map_2003.drop(index=[8], inplace=True)
map_2003.replace(state_dict, inplace=True)
map_2003.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2003 = px.choropleth(map_2003, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "Reds")
fig_2003.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2003')
fig_2003.update_geos(bgcolor='#0E1117')

map_2004 = df_2004.copy()
map_2004.drop(index=[8], inplace=True)
map_2004.replace(state_dict, inplace=True)
map_2004.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2004 = px.choropleth(map_2004, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "Reds")
fig_2004.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2004')
fig_2004.update_geos(bgcolor='#0E1117')

map_2005 = df_2005.copy()
map_2005.drop(index=[8], inplace=True)
map_2005.replace(state_dict, inplace=True)
map_2005.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2005 = px.choropleth(map_2005, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "Reds")
fig_2005.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2005')
fig_2005.update_geos(bgcolor='#0E1117')

map_2006 = df_2006.copy()
map_2006.drop(index=[8], inplace=True)
map_2006.replace(state_dict, inplace=True)
map_2006.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2006 = px.choropleth(map_2006, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "Reds")
fig_2006.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2006')
fig_2006.update_geos(bgcolor='#0E1117')

map_2007 = df_2007.copy()
map_2007.drop(index=[8], inplace=True)
map_2007.replace(state_dict, inplace=True)
map_2007.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2007 = px.choropleth(map_2007, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "Reds")
fig_2007.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2007')
fig_2007.update_geos(bgcolor='#0E1117')

map_2008 = df_2008.copy()
map_2008.drop(index=[8], inplace=True)
map_2008.replace(state_dict, inplace=True)
map_2008.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2008 = px.choropleth(map_2008, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "Reds")
fig_2008.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2008')
fig_2008.update_geos(bgcolor='#0E1117')

map_2009 = df_2009.copy()
map_2009.drop(index=[8], inplace=True)
map_2009.replace(state_dict, inplace=True)
map_2009.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2009 = px.choropleth(map_2009, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "Reds")
fig_2009.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2009')
fig_2009.update_geos(bgcolor='#0E1117')

map_2010 = df_2010.copy()
map_2010.drop(index=[8], inplace=True)
map_2010.replace(state_dict, inplace=True)
map_2010.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2010 = px.choropleth(map_2010, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "Reds")
fig_2010.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2010')
fig_2010.update_geos(bgcolor='#0E1117')

map_2011 = df_2011.copy()
map_2011.drop(index=[8], inplace=True)
map_2011.replace(state_dict, inplace=True)
map_2011.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2011 = px.choropleth(map_2011, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "Reds")
fig_2011.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2011')
fig_2011.update_geos(bgcolor='#0E1117')

map_2012 = df_2012.copy()
map_2012.drop(index=[8], inplace=True)
map_2012.replace(state_dict, inplace=True)
map_2012.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2012 = px.choropleth(map_2012, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "Reds")
fig_2012.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2012')
fig_2012.update_geos(bgcolor='#0E1117')

map_2013 = df_2013.copy()
map_2013.drop(index=[8], inplace=True)
map_2013.replace(state_dict, inplace=True)
map_2013.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2013 = px.choropleth(map_2013, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "Reds")
fig_2013.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2013')
fig_2013.update_geos(bgcolor='#0E1117')

map_2014 = df_2014.copy()
map_2014.drop(index=[8], inplace=True)
map_2014.replace(state_dict, inplace=True)
map_2014.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2014 = px.choropleth(map_2014, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "Reds")
fig_2014.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2014')
fig_2014.update_geos(bgcolor='#0E1117')

map_2015 = df_2015.copy()
map_2015.drop(index=[8], inplace=True)
map_2015.replace(state_dict, inplace=True)
map_2015.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2015 = px.choropleth(map_2015, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "Reds")
fig_2015.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2015')
fig_2015.update_geos(bgcolor='#0E1117')

map_2016 = df_2016.copy()
map_2016.drop(index=[8], inplace=True)
map_2016.replace(state_dict, inplace=True)
map_2016.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2016 = px.choropleth(map_2016, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "Reds")
fig_2016.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2016')
fig_2016.update_geos(bgcolor='#0E1117')

map_2017 = df_2017.copy()
map_2017.drop(index=[8], inplace=True)
map_2017.replace(state_dict, inplace=True)
map_2017.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2017 = px.choropleth(map_2017, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "Reds")
fig_2017.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2017')
fig_2017.update_geos(bgcolor='#0E1117')

map_2018 = df_2018.copy()
map_2018.drop(index=[8], inplace=True)
map_2018.replace(state_dict, inplace=True)
map_2018.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2018 = px.choropleth(map_2018, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "Reds")
fig_2018.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2018')
fig_2018.update_geos(bgcolor='#0E1117')

map_2019 = df_2019.copy()
map_2019.drop(index=[8], inplace=True)
map_2019.replace(state_dict, inplace=True)
map_2019.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2019 = px.choropleth(map_2019, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "Reds")
fig_2019.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2019')
fig_2019.update_geos(bgcolor='#0E1117')

map_2020 = df_2020.copy()
map_2020.drop(index=[8], inplace=True)
map_2020.replace(state_dict, inplace=True)
map_2020.rename(columns={"state":"State", "total_incidents_per_capita":"Per Capita"}, inplace=True)

fig_2020 = px.choropleth(map_2020, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Per Capita", 
                         color_continuous_scale = "Reds")
fig_2020.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in 2020')
fig_2020.update_geos(bgcolor='#0E1117')

# prep data for us total line chart

us_totals = pd.read_csv(r"C:\Users\14802\Desktop\hate-crime analysis\working_notebooks\EDA\us_per_cap_totals.csv")

us_totals.year = us_totals.year.astype(str) # years need to be strings or Altair puts commas in the values

source_us_totals = us_totals.copy() # makes copy of us dataframe to be used as chart source

nearest = alt.selection(type='single', nearest=True, on='mouseover', fields=['year'], empty='none') # creates interactivity on mouseover of chart

line_us_data = alt.Chart(source_us_totals).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('total_incidents_per_capita', axis=alt.Axis(title="Hate Crimes Per Capita")))

selectors = alt.Chart(source_us_totals).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)

points = line_us_data.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))

text = line_us_data.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'total_incidents_per_capita', alt.value(' ')))

rules = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)

us_chart = alt.layer(line_us_data, selectors, points, rules, text).properties(width=700, height=400).configure_axis(labelFontSize=18, titleFontSize=18)


# prep data for state line charts

state_df = pd.read_csv(r"C:\Users\14802\Desktop\hate-crime analysis\working_notebooks\EDA\state_totals_by_year.csv")
state_df.year = state_df.year.astype(str)
state_df.columns = state_df.columns.str.lower()

# Alabama Line Chart
alabama_df = state_df[['year', 'alabama']].copy()

line_alabama = alt.Chart(alabama_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('alabama', axis=alt.Axis(title="Alabama Hate Crimes Per Capita")))
selectors_alabama = alt.Chart(alabama_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_alabama = line_alabama.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_alabama = line_alabama.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'alabama', alt.value(' ')))
rules_alabama = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
alabama_chart = alt.layer(line_alabama, selectors_alabama, points_alabama, rules_alabama, text_alabama).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Alaska Line Chart
alaska_df = state_df[['year', 'alaska']].copy()

line_alaska = alt.Chart(alaska_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('alaska', axis=alt.Axis(title="Alaska Hate Crimes Per Capita")))
selectors_alaska = alt.Chart(alaska_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_alaska = line_alaska.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_alaska = line_alaska.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'alaska', alt.value(' ')))
rules_alaska = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
alaska_chart = alt.layer(line_alaska, selectors_alaska, points_alaska, rules_alaska, text_alaska).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Arizona Line Chart
arizona_df = state_df[['year', 'arizona']].copy()

line_arizona = alt.Chart(arizona_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('arizona', axis=alt.Axis(title="Arizona Hate Crimes Per Capita")))
selectors_arizona = alt.Chart(arizona_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_arizona = line_arizona.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_arizona = line_arizona.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'arizona', alt.value(' ')))
rules_arizona = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
arizona_chart = alt.layer(line_arizona, selectors_arizona, points_arizona, rules_arizona, text_arizona).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)


# Arkansas Line Chart
arkansas_df = state_df[['year', 'arkansas']].copy()

line_arkansas = alt.Chart(arkansas_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('arkansas', axis=alt.Axis(title="Arkansas Hate Crimes Per Capita")))
selectors_arkansas = alt.Chart(arkansas_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_arkansas = line_arkansas.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_arkansas = line_arkansas.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'arkansas', alt.value(' ')))
rules_arkansas = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
arkansas_chart = alt.layer(line_arkansas, selectors_arkansas, points_arkansas, rules_arkansas, text_arkansas).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)


# California Line Chart

california_df = state_df[['year', 'california']].copy()

line_california = alt.Chart(california_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('california', axis=alt.Axis(title="California Hate Crimes Per Capita")))
selectors_california = alt.Chart(california_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_california = line_california.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_california = line_california.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'california', alt.value(' ')))
rules_california = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
california_chart = alt.layer(line_california, selectors_california, points_california, rules_california, text_california).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Colorado Line Chart

colorado_df = state_df[['year', 'colorado']].copy()

line_colorado = alt.Chart(colorado_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('colorado', axis=alt.Axis(title="Colorado Hate Crimes Per Capita")))
selectors_colorado = alt.Chart(colorado_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_colorado = line_colorado.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_colorado = line_colorado.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'colorado', alt.value(' ')))
rules_colorado = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
colorado_chart = alt.layer(line_colorado, selectors_colorado, points_colorado, rules_colorado, text_colorado).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Connecticut Line Chart
connecticut_df = state_df[['year', 'connecticut']].copy()

line_connecticut = alt.Chart(connecticut_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('connecticut', axis=alt.Axis(title="Connecticut Hate Crimes Per Capita")))
selectors_connecticut = alt.Chart(connecticut_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_connecticut = line_connecticut.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_connecticut = line_connecticut.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'connecticut', alt.value(' ')))
rules_connecticut = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
connecticut_chart = alt.layer(line_connecticut, selectors_connecticut, points_connecticut, rules_connecticut, text_connecticut).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)


# Delaware Line Chart
delaware_df = state_df[['year', 'delaware']].copy()

line_delaware = alt.Chart(delaware_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('delaware', axis=alt.Axis(title="Delaware Hate Crimes Per Capita")))
selectors_delaware = alt.Chart(delaware_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_delaware = line_delaware.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_delaware = line_delaware.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'delaware', alt.value(' ')))
rules_delaware = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
delaware_chart = alt.layer(line_delaware, selectors_delaware, points_delaware, rules_delaware, text_delaware).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)


# District of Columbia Line Chart
dc_df = state_df[['year', 'district of columbia']].copy()

line_dc = alt.Chart(dc_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('district of columbia', axis=alt.Axis(title="District of Columbia Hate Crimes Per Capita")))
selectors_dc = alt.Chart(dc_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_dc = line_dc.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_dc = line_dc.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'district of columbia', alt.value(' ')))
rules_dc = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
dc_chart = alt.layer(line_dc, selectors_dc, points_dc, rules_dc, text_dc).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Florida Line Chart

florida_df = state_df[['year', 'florida']].copy()

line_florida = alt.Chart(florida_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('florida', axis=alt.Axis(title="Florida Hate Crimes Per Capita")))
selectors_florida = alt.Chart(florida_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_florida = line_florida.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_florida = line_florida.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'florida', alt.value(' ')))
rules_florida = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
florida_chart = alt.layer(line_florida, selectors_florida, points_florida, rules_florida, text_florida).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Georgia Line Chart

georgia_df = state_df[['year', 'georgia']].copy()

line_georgia = alt.Chart(georgia_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('georgia', axis=alt.Axis(title="Georgia Hate Crimes Per Capita")))
selectors_georgia = alt.Chart(georgia_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_georgia = line_georgia.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_georgia = line_georgia.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'georgia', alt.value(' ')))
rules_georgia = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
georgia_chart = alt.layer(line_georgia, selectors_georgia, points_georgia, rules_georgia, text_georgia).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Idaho Line Chart

idaho_df = state_df[['year', 'idaho']].copy()

line_idaho = alt.Chart(idaho_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('idaho', axis=alt.Axis(title="Idaho Hate Crimes Per Capita")))
selectors_idaho = alt.Chart(idaho_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_idaho = line_idaho.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_idaho = line_idaho.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'idaho', alt.value(' ')))
rules_idaho = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
idaho_chart = alt.layer(line_idaho, selectors_idaho, points_idaho, rules_idaho, text_idaho).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Illinois Line Chart

illinois_df = state_df[['year', 'illinois']].copy()

line_illinois = alt.Chart(illinois_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('illinois', axis=alt.Axis(title="Illinois Hate Crimes Per Capita")))
selectors_illinois = alt.Chart(illinois_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_illinois = line_illinois.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_illinois = line_illinois.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'illinois', alt.value(' ')))
rules_illinois = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
illinois_chart = alt.layer(line_illinois, selectors_illinois, points_illinois, rules_illinois, text_illinois).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Indiana Line Chart

indiana_df = state_df[['year', 'indiana']].copy()

line_indiana = alt.Chart(indiana_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('indiana', axis=alt.Axis(title="Indiana Hate Crimes Per Capita")))
selectors_indiana = alt.Chart(indiana_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_indiana = line_indiana.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_indiana = line_indiana.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'indiana', alt.value(' ')))
rules_indiana = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
indiana_chart = alt.layer(line_indiana, selectors_indiana, points_indiana, rules_indiana, text_indiana).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Iowa Line Chart

iowa_df = state_df[['year', 'iowa']].copy()

line_iowa = alt.Chart(iowa_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('iowa', axis=alt.Axis(title="Iowa Hate Crimes Per Capita")))
selectors_iowa = alt.Chart(iowa_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_iowa = line_iowa.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_iowa = line_iowa.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'iowa', alt.value(' ')))
rules_iowa = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
iowa_chart = alt.layer(line_iowa, selectors_iowa, points_iowa, rules_iowa, text_iowa).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Kansas Line Chart

kansas_df = state_df[['year', 'kansas']].copy()

line_kansas = alt.Chart(kansas_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('kansas', axis=alt.Axis(title="Kansas Hate Crimes Per Capita")))
selectors_kansas = alt.Chart(kansas_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_kansas = line_kansas.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_kansas = line_kansas.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'kansas', alt.value(' ')))
rules_kansas = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
kansas_chart = alt.layer(line_kansas, selectors_kansas, points_kansas, rules_kansas, text_kansas).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Kentucky Line Chart

kentucky_df = state_df[['year', 'kentucky']].copy()

line_kentucky = alt.Chart(kentucky_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('kentucky', axis=alt.Axis(title="Kentucky Hate Crimes Per Capita")))
selectors_kentucky = alt.Chart(kentucky_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_kentucky = line_kentucky.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_kentucky = line_kentucky.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'kentucky', alt.value(' ')))
rules_kentucky = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
kentucky_chart = alt.layer(line_kentucky, selectors_kentucky, points_kentucky, rules_kentucky, text_kentucky).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Louisiana Line Chart

louisiana_df = state_df[['year', 'louisiana']].copy()

line_louisiana = alt.Chart(louisiana_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('louisiana', axis=alt.Axis(title="Louisiana Hate Crimes Per Capita")))
selectors_louisiana = alt.Chart(louisiana_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_louisiana = line_louisiana.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_louisiana = line_louisiana.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'louisiana', alt.value(' ')))
rules_louisiana = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
louisiana_chart = alt.layer(line_louisiana, selectors_louisiana, points_louisiana, rules_louisiana, text_louisiana).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Maine Line Chart

maine_df = state_df[['year', 'maine']].copy()

line_maine = alt.Chart(maine_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('maine', axis=alt.Axis(title="Maine Hate Crimes Per Capita")))
selectors_maine = alt.Chart(maine_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_maine = line_maine.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_maine = line_maine.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'maine', alt.value(' ')))
rules_maine = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
maine_chart = alt.layer(line_maine, selectors_maine, points_maine, rules_maine, text_maine).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Maryland Line Chart

maryland_df = state_df[['year', 'maryland']].copy()

line_maryland = alt.Chart(maryland_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('maryland', axis=alt.Axis(title="Maryland Hate Crimes Per Capita")))
selectors_maryland = alt.Chart(maryland_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_maryland = line_maryland.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_maryland = line_maryland.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'maryland', alt.value(' ')))
rules_maryland = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
maryland_chart = alt.layer(line_maryland, selectors_maryland, points_maryland, rules_maryland, text_maryland).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Massachusetts Line Chart

massachusetts_df = state_df[['year', 'massachusetts']].copy()

line_massachusetts = alt.Chart(massachusetts_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('massachusetts', axis=alt.Axis(title="Mass. Hate Crimes Per Capita")))
selectors_massachusetts = alt.Chart(massachusetts_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_massachusetts = line_massachusetts.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_massachusetts = line_massachusetts.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'massachusetts', alt.value(' ')))
rules_massachusetts = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
massachusetts_chart = alt.layer(line_massachusetts, selectors_massachusetts, points_massachusetts, rules_massachusetts, text_massachusetts).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Michigan Line Chart

michigan_df = state_df[['year', 'michigan']].copy()

line_michigan = alt.Chart(michigan_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('michigan', axis=alt.Axis(title="Michigan Hate Crimes Per Capita")))
selectors_michigan = alt.Chart(michigan_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_michigan = line_michigan.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_michigan = line_michigan.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'michigan', alt.value(' ')))
rules_michigan = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
michigan_chart = alt.layer(line_michigan, selectors_michigan, points_michigan, rules_michigan, text_michigan).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Minnesota Line Chart

minnesota_df = state_df[['year', 'minnesota']].copy()

line_minnesota = alt.Chart(minnesota_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('minnesota', axis=alt.Axis(title="Minnesota Hate Crimes Per Capita")))
selectors_minnesota = alt.Chart(minnesota_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_minnesota = line_minnesota.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_minnesota = line_minnesota.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'minnesota', alt.value(' ')))
rules_minnesota = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
minnesota_chart = alt.layer(line_minnesota, selectors_minnesota, points_minnesota, rules_minnesota, text_minnesota).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Mississippi Line Chart

mississippi_df = state_df[['year', 'mississippi']].copy()

line_mississippi = alt.Chart(mississippi_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('mississippi', axis=alt.Axis(title="Mississippi Hate Crimes Per Capita")))
selectors_mississippi = alt.Chart(mississippi_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_mississippi = line_mississippi.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_mississippi = line_mississippi.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'mississippi', alt.value(' ')))
rules_mississippi = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
mississippi_chart = alt.layer(line_mississippi, selectors_mississippi, points_mississippi, rules_mississippi, text_mississippi).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Missouri Line Chart

missouri_df = state_df[['year', 'missouri']].copy()

line_missouri = alt.Chart(missouri_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('missouri', axis=alt.Axis(title="Missouri Hate Crimes Per Capita")))
selectors_missouri = alt.Chart(missouri_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_missouri = line_missouri.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_missouri = line_missouri.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'missouri', alt.value(' ')))
rules_missouri = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
missouri_chart = alt.layer(line_missouri, selectors_missouri, points_missouri, rules_missouri, text_missouri).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Montana Line Chart

montana_df = state_df[['year', 'montana']].copy()

line_montana = alt.Chart(montana_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('montana', axis=alt.Axis(title="Montana Hate Crimes Per Capita")))
selectors_montana = alt.Chart(montana_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_montana = line_montana.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_montana = line_montana.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'montana', alt.value(' ')))
rules_montana = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
montana_chart = alt.layer(line_montana, selectors_montana, points_montana, rules_montana, text_montana).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Nebraska Line Chart

nebraska_df = state_df[['year', 'nebraska']].copy()

line_nebraska = alt.Chart(nebraska_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('nebraska', axis=alt.Axis(title="Nebraska Hate Crimes Per Capita")))
selectors_nebraska = alt.Chart(nebraska_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_nebraska = line_nebraska.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_nebraska = line_nebraska.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'nebraska', alt.value(' ')))
rules_nebraska = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
nebraska_chart = alt.layer(line_nebraska, selectors_nebraska, points_nebraska, rules_nebraska, text_nebraska).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Nevada Line Chart

nevada_df = state_df[['year', 'nevada']].copy()

line_nevada = alt.Chart(nevada_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('nevada', axis=alt.Axis(title="Nevada Hate Crimes Per Capita")))
selectors_nevada = alt.Chart(nevada_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_nevada = line_nevada.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_nevada = line_nevada.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'nevada', alt.value(' ')))
rules_nevada = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
nevada_chart = alt.layer(line_nevada, selectors_nevada, points_nevada, rules_nevada, text_nevada).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# New Hampshire Line Chart

nh_df = state_df[['year', 'new hampshire']].copy()

line_nh = alt.Chart(nh_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('new hampshire', axis=alt.Axis(title="New Hampshire Hate Crimes Per Capita")))
selectors_nh = alt.Chart(nh_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_nh = line_nh.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_nh = line_nh.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'new hampshire', alt.value(' ')))
rules_nh = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
nh_chart = alt.layer(line_nh, selectors_nh, points_nh, rules_nh, text_nh).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# New Jersey Line Chart

nj_df = state_df[['year', 'new jersey']].copy()

line_nj = alt.Chart(nj_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('new jersey', axis=alt.Axis(title="New Jersey Hate Crimes Per Capita")))
selectors_nj = alt.Chart(nj_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_nj = line_nj.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_nj = line_nj.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'new jersey', alt.value(' ')))
rules_nj = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
nj_chart = alt.layer(line_nj, selectors_nj, points_nj, rules_nj, text_nj).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# New Mexico Line Chart

nm_df = state_df[['year', 'new mexico']].copy()

line_nm = alt.Chart(nm_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('new mexico', axis=alt.Axis(title="New Mexico Hate Crimes Per Capita")))
selectors_nm = alt.Chart(nm_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_nm = line_nm.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_nm = line_nm.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'new mexico', alt.value(' ')))
rules_nm = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
nm_chart = alt.layer(line_nm, selectors_nm, points_nm, rules_nm, text_nm).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# New York Line Chart

ny_df = state_df[['year', 'new york']].copy()

line_ny = alt.Chart(ny_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('new york', axis=alt.Axis(title="New York Hate Crimes Per Capita")))
selectors_ny = alt.Chart(ny_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_ny = line_ny.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_ny = line_ny.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'new york', alt.value(' ')))
rules_ny = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
ny_chart = alt.layer(line_ny, selectors_ny, points_ny, rules_ny, text_ny).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# North Carolina Line Chart

nc_df = state_df[['year', 'north carolina']].copy()

line_nc = alt.Chart(nc_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('north carolina', axis=alt.Axis(title="N.C. Hate Crimes Per Capita")))
selectors_nc = alt.Chart(nc_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_nc = line_nc.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_nc = line_nc.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'north carolina', alt.value(' ')))
rules_nc = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
nc_chart = alt.layer(line_nc, selectors_nc, points_nc, rules_nc, text_nc).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# North Dakota Line Chart

nd_df = state_df[['year', 'north dakota']].copy()

line_nd = alt.Chart(nd_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('north dakota', axis=alt.Axis(title="N. Dakota Hate Crimes Per Capita")))
selectors_nd = alt.Chart(nd_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_nd = line_nd.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_nd = line_nd.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'north dakota', alt.value(' ')))
rules_nd = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
nd_chart = alt.layer(line_nd, selectors_nd, points_nd, rules_nd, text_nd).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Ohio Line Chart
ohio_df = state_df[['year', 'ohio']].copy()

line_ohio = alt.Chart(ohio_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('ohio', axis=alt.Axis(title="Ohio Hate Crimes Per Capita")))
selectors_ohio = alt.Chart(ohio_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_ohio = line_ohio.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_ohio = line_ohio.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'ohio', alt.value(' ')))
rules_ohio = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
ohio_chart = alt.layer(line_ohio, selectors_ohio, points_ohio, rules_ohio, text_ohio).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Oklahoma Line Chart

oklahoma_df = state_df[['year', 'oklahoma']].copy()

line_oklahoma = alt.Chart(oklahoma_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('oklahoma', axis=alt.Axis(title="Oklahoma Hate Crimes Per Capita")))
selectors_oklahoma = alt.Chart(oklahoma_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_oklahoma = line_oklahoma.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_oklahoma = line_oklahoma.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'oklahoma', alt.value(' ')))
rules_oklahoma = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
oklahoma_chart = alt.layer(line_oklahoma, selectors_oklahoma, points_oklahoma, rules_oklahoma, text_oklahoma).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Oregon Line Chart

oregon_df = state_df[['year', 'oregon']].copy()

line_oregon = alt.Chart(oregon_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('oregon', axis=alt.Axis(title="Oregon Hate Crimes Per Capita")))
selectors_oregon = alt.Chart(oregon_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_oregon = line_oregon.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_oregon = line_oregon.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'oregon', alt.value(' ')))
rules_oregon = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
oregon_chart = alt.layer(line_oregon, selectors_oregon, points_oregon, rules_oregon, text_oregon).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Pennsylvania Line Chart

pennsylvania_df = state_df[['year', 'pennsylvania']].copy()

line_pennsylvania = alt.Chart(pennsylvania_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('pennsylvania', axis=alt.Axis(title="Pennsylvania Hate Crimes Per Capita")))
selectors_pennsylvania = alt.Chart(pennsylvania_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_pennsylvania = line_pennsylvania.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_pennsylvania = line_pennsylvania.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'pennsylvania', alt.value(' ')))
rules_pennsylvania = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
pennsylvania_chart = alt.layer(line_pennsylvania, selectors_pennsylvania, points_pennsylvania, rules_pennsylvania, text_pennsylvania).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Rhode Island Line Chart

ri_df = state_df[['year', 'rhode island']].copy()

line_ri = alt.Chart(ri_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('rhode island', axis=alt.Axis(title="Rhode Island Hate Crimes Per Capita")))
selectors_ri = alt.Chart(ri_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_ri = line_ri.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_ri = line_ri.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'rhode island', alt.value(' ')))
rules_ri = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
ri_chart = alt.layer(line_ri, selectors_ri, points_ri, rules_ri, text_ri).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# South Carolina Line Chart

sc_df = state_df[['year', 'south carolina']].copy()

line_sc = alt.Chart(sc_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('south carolina', axis=alt.Axis(title="S. Carolina Hate Crimes Per Capita")))
selectors_sc = alt.Chart(sc_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_sc = line_sc.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_sc = line_sc.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'south carolina', alt.value(' ')))
rules_sc = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
sc_chart = alt.layer(line_sc, selectors_sc, points_sc, rules_sc, text_sc).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# South Dakota Line Chart

sd_df = state_df[['year', 'south dakota']].copy()

line_sd = alt.Chart(sd_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('south dakota', axis=alt.Axis(title="S. Dakota Hate Crimes Per Capita")))
selectors_sd = alt.Chart(sd_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_sd = line_sd.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_sd = line_sd.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'south dakota', alt.value(' ')))
rules_sd = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
sd_chart = alt.layer(line_sd, selectors_sd, points_sd, rules_sd, text_sd).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Tennessee Line Chart

tennessee_df = state_df[['year', 'tennessee']].copy()

line_tennessee = alt.Chart(tennessee_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('tennessee', axis=alt.Axis(title="Tennessee Hate Crimes Per Capita")))
selectors_tennessee = alt.Chart(tennessee_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_tennessee = line_tennessee.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_tennessee = line_tennessee.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'tennessee', alt.value(' ')))
rules_tennessee = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
tennessee_chart = alt.layer(line_tennessee, selectors_tennessee, points_tennessee, rules_tennessee, text_tennessee).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Texas Line Chart

texas_df = state_df[['year', 'texas']].copy()

line_texas = alt.Chart(texas_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('texas', axis=alt.Axis(title="Texas Hate Crimes Per Capita")))
selectors_texas = alt.Chart(texas_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_texas = line_texas.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_texas = line_texas.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'texas', alt.value(' ')))
rules_texas = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
texas_chart = alt.layer(line_texas, selectors_texas, points_texas, rules_texas, text_texas).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Utah Line Chart

utah_df = state_df[['year', 'utah']].copy()

line_utah = alt.Chart(utah_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('utah', axis=alt.Axis(title="Utah Hate Crimes Per Capita")))
selectors_utah = alt.Chart(utah_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_utah = line_utah.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_utah = line_utah.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'utah', alt.value(' ')))
rules_utah = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
utah_chart = alt.layer(line_utah, selectors_utah, points_utah, rules_utah, text_utah).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Vermont Line Chart

vermont_df = state_df[['year', 'vermont']].copy()

line_vermont = alt.Chart(vermont_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('vermont', axis=alt.Axis(title="Vermont Hate Crimes Per Capita")))
selectors_vermont = alt.Chart(vermont_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_vermont = line_vermont.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_vermont = line_vermont.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'vermont', alt.value(' ')))
rules_vermont = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
vermont_chart = alt.layer(line_vermont, selectors_vermont, points_vermont, rules_vermont, text_vermont).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Virginia Line Chart

virginia_df = state_df[['year', 'virginia']].copy()

line_virginia = alt.Chart(virginia_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('virginia', axis=alt.Axis(title="Virginia Hate Crimes Per Capita")))
selectors_virginia = alt.Chart(virginia_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_virginia = line_virginia.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_virginia = line_virginia.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'virginia', alt.value(' ')))
rules_virginia = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
virginia_chart = alt.layer(line_virginia, selectors_virginia, points_virginia, rules_virginia, text_virginia).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Washington Line Chart

washington_df = state_df[['year', 'washington']].copy()

line_washington = alt.Chart(washington_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('washington', axis=alt.Axis(title="Washington Hate Crimes Per Capita")))
selectors_washington = alt.Chart(washington_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_washington = line_washington.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_washington = line_washington.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'washington', alt.value(' ')))
rules_washington = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
washington_chart = alt.layer(line_washington, selectors_washington, points_washington, rules_washington, text_washington).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# West Virginia Line Chart

wv_df = state_df[['year', 'west virginia']].copy()

line_wv = alt.Chart(wv_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('west virginia', axis=alt.Axis(title="W. Virginia Hate Crimes Per Capita")))
selectors_wv = alt.Chart(wv_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_wv = line_wv.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_wv = line_wv.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'west virginia', alt.value(' ')))
rules_wv = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
wv_chart = alt.layer(line_wv, selectors_wv, points_wv, rules_wv, text_wv).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Wisconsin Line Chart

wisconsin_df = state_df[['year', 'wisconsin']].copy()

line_wisconsin = alt.Chart(wisconsin_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('wisconsin', axis=alt.Axis(title="Wisconsin Hate Crimes Per Capita")))
selectors_wisconsin = alt.Chart(wisconsin_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_wisconsin = line_wisconsin.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_wisconsin = line_wisconsin.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'wisconsin', alt.value(' ')))
rules_wisconsin = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
wisconsin_chart = alt.layer(line_wisconsin, selectors_wisconsin, points_wisconsin, rules_wisconsin, text_wisconsin).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)

# Wyoming Line Chart

wyoming_df = state_df[['year', 'wyoming']].copy()

line_wyoming = alt.Chart(wyoming_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y('wyoming', axis=alt.Axis(title="Wyoming Hate Crimes Per Capita")))
selectors_wyoming = alt.Chart(wyoming_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
points_wyoming = line_wyoming.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
text_wyoming = line_wyoming.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, 'wyoming', alt.value(' ')))
rules_wyoming = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
wyoming_chart = alt.layer(line_wyoming, selectors_wyoming, points_wyoming, rules_wyoming, text_wyoming).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)



##########################  STREAMLIT FRONT END VIEW ####################################


# main title
st.title("U.S. Hate Crime Data Analysis") 

# us total - line chart

st.subheader("Total Hate Crimes Per Capita in U.S. from 2000-2020")
st.caption("(Per capita values are shown per 100,000 people)")

st.altair_chart(us_chart)



# state totals - line charts

st.subheader("Hate Crime Totals by State")
st.caption("(Per capita values are shown per 100,000 people)")

with st.expander("Click to Choose State"): 
# Alabama line chart
    if st.checkbox('Alabama'):
        st.altair_chart(alabama_chart)
# Alaska line chart    
    if st.checkbox('Alaska'):
        st.altair_chart(alaska_chart)
# Arizona line chart    
    if st.checkbox('Arizona'):
        st.altair_chart(arizona_chart)
# Arkansas line chart
    if st.checkbox('Arkansas'):
        st.altair_chart(arkansas_chart)
# California line chart    
    if st.checkbox('California'):
        st.altair_chart(california_chart)
# Colorado line chart
    if st.checkbox('Colorado'):
        st.altair_chart(colorado_chart)
# Connecticut line chart
    if st.checkbox('Connecticut'):
        st.altair_chart(connecticut_chart)
# Delaware line chart
    if st.checkbox('Delaware'):
        st.altair_chart(delaware_chart)
# D.C. line chart
    if st.checkbox('District of Columbia'):
        st.altair_chart(dc_chart)
# Florida Line Chart
    if st.checkbox('Florida'):
        st.altair_chart(florida_chart)
# Georgia Line Chart
    if st.checkbox('Georgia'):
        st.altair_chart(georgia_chart)
# Idaho Line Chart
    if st.checkbox('Idaho'):
        st.altair_chart(idaho_chart)
# Illinois Line Chart
    if st.checkbox('Illinois'):
        st.altair_chart(illinois_chart)
# Indiana Line Chart
    if st.checkbox('Indiana'):
        st.altair_chart(indiana_chart)
# Iowa Line Chart
    if st.checkbox('Iowa'):
        st.altair_chart(iowa_chart)
# Kansas Line Chart
    if st.checkbox('Kansas'):
        st.altair_chart(kansas_chart)
# Kentucky Line Chart
    if st.checkbox('Kentucky'):
        st.altair_chart(kentucky_chart)
# Louisiana Line Chart
    if st.checkbox('Louisiana'):
        st.altair_chart(louisiana_chart)
# Maine Line Chart
    if st.checkbox('Maine'):
        st.altair_chart(maine_chart)
# Maryland Line Chart
    if st.checkbox('Maryland'):
        st.altair_chart(maryland_chart)
# Massachusetts Line Chart
    if st.checkbox('Massachusetts'):
        st.altair_chart(massachusetts_chart)
# Michigan Line Chart
    if st.checkbox('Michigan'):
        st.altair_chart(michigan_chart)
# Minnesota Line Chart
    if st.checkbox('Minnesota'):
        st.altair_chart(minnesota_chart)
# Mississippi Line Chart
    if st.checkbox('Mississippi'):
        st.altair_chart(mississippi_chart)
# Missouri Line Chart
    if st.checkbox('Missouri'):
        st.altair_chart(missouri_chart)
# Montana Line Chart
    if st.checkbox('Montana'):
        st.altair_chart(montana_chart)
# Nebraska Line Chart
    if st.checkbox('Nebraska'):
        st.altair_chart(nebraska_chart)
# Nevada Line Chart
    if st.checkbox('Nevada'):
        st.altair_chart(nevada_chart)
# New Hampshire Line Chart
    if st.checkbox('New Hampshire'):
        st.altair_chart(nh_chart)
# New Jersey Line Chart
    if st.checkbox('New Jersey'):
        st.altair_chart(nj_chart)
# New Mexico Line Chart
    if st.checkbox('New Mexico'):
        st.altair_chart(nm_chart)
# New York Line Chart
    if st.checkbox('New York'):
        st.altair_chart(ny_chart)
# North Carolina Line Chart
    if st.checkbox('North Carolina'):
        st.altair_chart(nc_chart)
# North Dakota Line Chart
    if st.checkbox('North Dakota'):
        st.altair_chart(nd_chart)
# Ohio Line Chart
    if st.checkbox('Ohio'):
        st.altair_chart(ohio_chart)
# Oklahoma Line Chart
    if st.checkbox('Oklahoma'):
        st.altair_chart(oklahoma_chart)
# Oregon Line Chart
    if st.checkbox('Oregon'):
        st.altair_chart(oregon_chart)
# Pennsylvania Line Chart
    if st.checkbox('Pennsylvania'):
        st.altair_chart(pennsylvania_chart)
# Rhode Island Line Chart
    if st.checkbox('Rhode Island'):
        st.altair_chart(ri_chart)
# South Carolina Line Chart
    if st.checkbox('South Carolina'):
        st.altair_chart(sc_chart)
# South Dakota Line Chart
    if st.checkbox('South Dakota'):
        st.altair_chart(sd_chart)
# Tennessee Line Chart
    if st.checkbox('Tennessee'):
        st.altair_chart(tennessee_chart)
# Texas Line Chart
    if st.checkbox('Texas'):
        st.altair_chart(texas_chart)
# Utah Line Chart
    if st.checkbox('Utah'):
        st.altair_chart(utah_chart)
# Vermont Line Chart
    if st.checkbox('Vermont'):
        st.altair_chart(vermont_chart)
# Virginia Line Chart
    if st.checkbox('Virginia'):
        st.altair_chart(virginia_chart)
# Washington Line Chart
    if st.checkbox('Washington'):
        st.altair_chart(washington_chart)
# West Virginia Line Chart
    if st.checkbox('West Virginia'):
        st.altair_chart(wv_chart)
# Wisconsin Line Chart
    if st.checkbox('Wisconsin'):
        st.altair_chart(wisconsin_chart)
# Wyoming Line Chart
    if st.checkbox('Wyoming'):
        st.altair_chart(wyoming_chart)



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
