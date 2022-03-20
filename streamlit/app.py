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

@st.cache(persist=True, allow_output_mutation=True)
def get_path(csv):
    return Path("datasets", csv)

csv_2000 = get_path("map_2000.csv")
csv_2001 = get_path("map_2001.csv")
csv_2002 = get_path("map_2002.csv")
csv_2003 = get_path("map_2003.csv")
csv_2004 = get_path("map_2004.csv")
csv_2005 = get_path("map_2005.csv")
csv_2006 = get_path("map_2006.csv")
csv_2007 = get_path("map_2007.csv")
csv_2008 = get_path("map_2008.csv")
csv_2009 = get_path("map_2009.csv")
csv_2010 = get_path("map_2010.csv")
csv_2011 = get_path("map_2011.csv")
csv_2012 = get_path("map_2012.csv")
csv_2013 = get_path("map_2013.csv")
csv_2014 = get_path("map_2014.csv")
csv_2015 = get_path("map_2015.csv")
csv_2016 = get_path("map_2016.csv")
csv_2017 = get_path("map_2017.csv")
csv_2018 = get_path("map_2018.csv")
csv_2019 = get_path("map_2019.csv")
csv_2020 = get_path("map_2020.csv")
pc_2000 = get_path("per_capita_2000.csv")
pc_2001 = get_path("per_capita_2001.csv")
pc_2002 = get_path("per_capita_2002.csv")
pc_2003 = get_path("per_capita_2003.csv")
pc_2004 = get_path("per_capita_2004.csv")
pc_2005 = get_path("per_capita_2005.csv")
pc_2006 = get_path("per_capita_2006.csv")
pc_2007 = get_path("per_capita_2007.csv")
pc_2008 = get_path("per_capita_2008.csv")
pc_2009 = get_path("per_capita_2009.csv")
pc_2010 = get_path("per_capita_2010.csv")
pc_2011 = get_path("per_capita_2011.csv")
pc_2012 = get_path("per_capita_2012.csv")
pc_2013 = get_path("per_capita_2013.csv")
pc_2014 = get_path("per_capita_2014.csv")
pc_2015 = get_path("per_capita_2015.csv")
pc_2016 = get_path("per_capita_2016.csv")
pc_2017 = get_path("per_capita_2017.csv")
pc_2018 = get_path("per_capita_2018.csv")
pc_2019 = get_path("per_capita_2019.csv")
pc_2020 = get_path("per_capita_2020.csv")
bias_csv = get_path("bias_per_capita.csv")
# loading data in for app 

@st.experimental_memo()
def get_csv(csv):
    return pd.read_csv(csv)


map_2000 = get_csv(csv_2000)
map_2001 = get_csv(csv_2001)
map_2002 = get_csv(csv_2002)
map_2003 = get_csv(csv_2003)
map_2004 = get_csv(csv_2004)
map_2005 = get_csv(csv_2005)
map_2006 = get_csv(csv_2006)
map_2007 = get_csv(csv_2007)
map_2008 = get_csv(csv_2008)
map_2009 = get_csv(csv_2009)
map_2010 = get_csv(csv_2010)
map_2011 = get_csv(csv_2011)
map_2012 = get_csv(csv_2012)
map_2013 = get_csv(csv_2013)
map_2014 = get_csv(csv_2014)
map_2015 = get_csv(csv_2015)
map_2016 = get_csv(csv_2016)
map_2017 = get_csv(csv_2017)
map_2018 = get_csv(csv_2018)
map_2019 = get_csv(csv_2019)
map_2020 = get_csv(csv_2020)
df_2000 = get_csv(pc_2000)
df_2001 = get_csv(pc_2001)
df_2002 = get_csv(pc_2002)
df_2003 = get_csv(pc_2003)
df_2004 = get_csv(pc_2004)
df_2005 = get_csv(pc_2005)
df_2006 = get_csv(pc_2006)
df_2007 = get_csv(pc_2007)
df_2008 = get_csv(pc_2008)
df_2009 = get_csv(pc_2009)
df_2010 = get_csv(pc_2010)
df_2011 = get_csv(pc_2011)
df_2012 = get_csv(pc_2012)
df_2013 = get_csv(pc_2013)
df_2014 = get_csv(pc_2014)
df_2015 = get_csv(pc_2015)
df_2016 = get_csv(pc_2016)
df_2017 = get_csv(pc_2017)
df_2018 = get_csv(pc_2018)
df_2019 = get_csv(pc_2019)
df_2020 = get_csv(pc_2020)
bias_df = get_csv(bias_csv)

bias_df.year = bias_df.year.astype(str)


# prep data for map visualizations

@st.experimental_memo()
def make_map(df, year):
    fig = px.choropleth(df, 
                            locations='State', 
                            locationmode="USA-states", 
                            scope="usa", 
                            color= "Per Capita", 
                            color_continuous_scale = "Reds",
                            height=500,
                            width=750)
    fig.update_layout(title_text=f'Total Reported Hate Crimes Per Capita Across the U.S. in {year}')
    fig.update_geos(bgcolor='#0E1117')
    return fig

fig_2000 = make_map(map_2000, 2000)
fig_2001 = make_map(map_2001, 2001)
fig_2002 = make_map(map_2002, 2002)
fig_2003 = make_map(map_2003, 2003)
fig_2004 = make_map(map_2004, 2004)
fig_2005 = make_map(map_2005, 2005)
fig_2006 = make_map(map_2006, 2006)
fig_2007 = make_map(map_2007, 2007)
fig_2008 = make_map(map_2008, 2008)
fig_2009 = make_map(map_2009, 2009)
fig_2010 = make_map(map_2010, 2010)
fig_2011 = make_map(map_2011, 2011)
fig_2012 = make_map(map_2012, 2012)
fig_2013 = make_map(map_2013, 2013)
fig_2014 = make_map(map_2014, 2014)
fig_2015 = make_map(map_2015, 2015)
fig_2016 = make_map(map_2016, 2016)
fig_2017 = make_map(map_2017, 2017)
fig_2018 = make_map(map_2018, 2018)
fig_2019 = make_map(map_2019, 2019)
fig_2020 = make_map(map_2020, 2020)



# prep data for us total line chart

us_totals_csv = get_path("us_per_cap_totals.csv")
us_totals = get_csv(us_totals_csv)

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

state_totals_csv = Path("datasets", "state_totals_by_year.csv")

state_df = pd.read_csv(state_totals_csv)
state_df.year = state_df.year.astype(str)
state_df.columns = state_df.columns.str.lower()

# Alabama Line Chart

@st.experimental_memo()
def make_state_line(state):
    line = alt.Chart(state_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y(f'{state}', axis=alt.Axis(title="Hate Crimes Per Capita")))
    selectors = alt.Chart(state_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
    points = line.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
    text = line.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, f'{state}', alt.value(' ')))
    rules = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
    chart = alt.layer(line, selectors, points, rules, text).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)
    return chart

alabama_chart = make_state_line('alabama')
alaska_chart = make_state_line('alaska')
arizona_chart = make_state_line('arizona')
arkansas_chart = make_state_line('arkansas')
california_chart = make_state_line('california')
colorado_chart = make_state_line('colorado')
connecticut_chart = make_state_line('connecticut')
delaware_chart = make_state_line('delaware')
dc_chart = make_state_line('district of columbia')
florida_chart = make_state_line('florida')
georgia_chart = make_state_line('georgia')
idaho_chart = make_state_line('idaho')
illinois_chart = make_state_line('illinois')
indiana_chart = make_state_line('indiana')
iowa_chart = make_state_line('iowa')
kansas_chart = make_state_line('kansas')
kentucky_chart = make_state_line('kentucky')
louisiana_chart = make_state_line('louisiana')
maine_chart = make_state_line('maine')
maryland_chart = make_state_line('maryland')
massachusetts_chart = make_state_line('massachusetts')
michigan_chart = make_state_line('michigan')
minnesota_chart = make_state_line('minnesota')
mississippi_chart = make_state_line('mississippi')
missouri_chart = make_state_line('missouri')
montana_chart = make_state_line('montana')
nebraska_chart = make_state_line('nebraska')
nevada_chart = make_state_line('nevada')
nh_chart = make_state_line('new hampshire')
nj_chart = make_state_line('new jersey')
ny_chart = make_state_line('new york')
nm_chart = make_state_line('new mexico')
nc_chart = make_state_line('north carolina')
nd_chart = make_state_line('north dakota')
ohio_chart = make_state_line('ohio')
oklahoma_chart = make_state_line('oklahoma')
oregon_chart = make_state_line('oregon')
pennsylvania_chart = make_state_line('pennsylvania')
ri_chart = make_state_line('rhode island')
sc_chart = make_state_line('south carolina')
sd_chart = make_state_line('south dakota')
tennessee_chart = make_state_line('tennessee')
texas_chart = make_state_line('texas')
utah_chart = make_state_line('utah')
vermont_chart = make_state_line('vermont')
virginia_chart = make_state_line('virginia')
washington_chart = make_state_line('washington')
wv_chart = make_state_line('west virginia')
wisconsin_chart = make_state_line('wisconsin')
wyoming_chart = make_state_line('wyoming')

###### prep raw tables ######

@st.experimental_memo()
def get_table(df):
    table = df[['state', 'total_incidents_per_capita']]
    return table

table_2000 = get_table(df_2000)
table_2001 = get_table(df_2001)
table_2002 = get_table(df_2002)
table_2003 = get_table(df_2003)
table_2004 = get_table(df_2004)
table_2005 = get_table(df_2005)
table_2006 = get_table(df_2006)
table_2007 = get_table(df_2007)
table_2008 = get_table(df_2008)
table_2009 = get_table(df_2009)
table_2010 = get_table(df_2010)
table_2011 = get_table(df_2011)
table_2012 = get_table(df_2012)
table_2013 = get_table(df_2013)
table_2014 = get_table(df_2014)
table_2015 = get_table(df_2015)
table_2016 = get_table(df_2016)
table_2017 = get_table(df_2017)
table_2018 = get_table(df_2018)
table_2019 = get_table(df_2019)
table_2020 = get_table(df_2020)

###### prep bias charts ####

@st.experimental_memo()
def make_bias_line(bias):
    line = alt.Chart(bias_df).mark_line(interpolate='basis').encode(alt.X('year',axis=alt.Axis(title="Year")), alt.Y(f'{bias}', axis=alt.Axis(title="Hate Crimes Per Capita")))
    selectors = alt.Chart(bias_df).mark_point().encode(x='year', opacity=alt.value(0),).add_selection(nearest)
    points = line.mark_point().encode(opacity=alt.condition(nearest, alt.value(1), alt.value(0)))
    text = line.mark_text(align='left', dx=5, dy=-5, color='white').encode(text=alt.condition(nearest, f'{bias}', alt.value(' ')))
    rules = alt.Chart(source_us_totals).mark_rule(color='gray').encode(x='year',).transform_filter(nearest)
    chart = alt.layer(line, selectors, points, rules, text).properties(width=600, height=400).configure_axis(labelFontSize=18, titleFontSize=18)
    return chart

anti_american_indian_or_alaska_native = make_bias_line("anti_american_indian_or_alaska_native")
anti_arab = make_bias_line("anti_arab") 
anti_asian = make_bias_line("anti_asian")
anti_atheism_agnosticism = make_bias_line("anti_atheism_agnosticism")
anti_bisexual = make_bias_line("anti_bisexual")
anti_black_or_african_american = make_bias_line("anti_black_or_african_american")
anti_buddhist = make_bias_line("anti_buddhist")
anti_catholic = make_bias_line("anti_catholic")
anti_eastern_orthodox_russian_greek_other = make_bias_line("anti_eastern_orthodox_russian_greek_other")
anti_female  = make_bias_line("anti_female")
anti_gay_male  = make_bias_line("anti_gay_male")
anti_gender_non_conforming  = make_bias_line("anti_gender_non_conforming")
anti_heterosexual  = make_bias_line("anti_heterosexual")
anti_hindu  = make_bias_line("anti-hindu")
anti_hispanic_or_latino  = make_bias_line("anti_hispanic_or_latino")
anti_islamic_muslim  = make_bias_line("anti_islamic_muslim")
anti_jehovahs_witness  = make_bias_line("anti_jehovahs_witness")
anti_jewish = make_bias_line("anti_jewish")
anti_lesbian_female = make_bias_line("anti_lesbian_female")
anti_male = make_bias_line("anti_male")
anti_mental_disability = make_bias_line("anti_mental_disability")
anti_mormon = make_bias_line("anti_mormon")
anti_native_hawaiian_or_other_pacific_islander = make_bias_line("anti_native_hawaiian_or_other_pacific_islander")
anti_physical_disability = make_bias_line("anti_physical_disability")
anti_protestant = make_bias_line("anti_protestant")
anti_sikh = make_bias_line("anti_sikh")
anti_transgender = make_bias_line("anti_transgender")
anti_white = make_bias_line("anti_white")
anti_lgbtq_grouped = make_bias_line("anti_lgbtq_grouped")

##########################  STREAMLIT FRONT END VIEW ####################################


# main title
st.title("U.S. Hate Crime Data Analysis") 

# side bar 
with st.sidebar:
    st.write("Welcome! Use the drop down menus below to select which data you would like to see.")
incident_totals_selection = st.sidebar.selectbox("Total Hate Crimes Per Capita:", ("Select Data", "U.S. Totals", "State Totals", "State Totals - Map Visualization", "State Totals - Raw Data"))
bias_totals_selection = st.sidebar.selectbox("Hate Crime Totals by Category:", ("Select Category", "All Bias Totals",
 'Anti-Arab',
 'Anti-Asian',
 'Anti-Atheist or Agnostic',
 'Anti-Bisexual',
 'Anti-Black or African American',
 'Anti-Buddhist',
 'Anti-Catholic',
 'Anti-Eastern Orthodox (Russian, Greek, and other)',
 'Anti-Female',
 'Anti-Gay (male)',
 'Anti-Gender Non-Conforming',
 'Anti-Heterosexual',
 'Anti-Hindu',
 'Anti-Hispanic or Latino',
 'Anti-Islamic (muslim)',
 'Anti-Jehovahs Witness',
 'Anti-Jewish',
 'Anti-Lesbian (female)',
 'Anti-Male',
 'Anti-Mental Disability',
 'Anti-Mormon',
 'Anti-Native American'
 'Anti-Pacific Islander',
 'Anti-Physical Disability',
 'Anti-Protestant',
 'Anti-Sikh',
 'Anti-Transgender',
 'Anti-White',
 'Anti-LGBTQ (grouped)'))

# us total - line chart

if incident_totals_selection == ("U.S. Totals"):
    st.subheader("Total Hate Crimes Per Capita in U.S. from 2000-2020")
    st.caption("(Per capita values are shown per 100,000 people)")

    st.altair_chart(us_chart)



# state totals - line charts

if incident_totals_selection == ("State Totals"):
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
if incident_totals_selection == ("State Totals - Map Visualization"):
    st.subheader('U.S. Map Density Chart')
    year = st.slider('Move slider to see data from each year', 2000, 2020, 2000)
        
    if year == 2000:
        st.write(fig_2000)
    if year == 2001:    
        st.write(fig_2001)
    if year == 2002:
        st.write(fig_2002)
    if year == 2003:    
        st.write(fig_2003)
    if year == 2004:
        st.write(fig_2004)
    if year == 2005:    
        st.write(fig_2005)
    if year == 2006:
        st.write(fig_2006)
    if year == 2007:    
        st.write(fig_2007)
    if year == 2008:    
        st.write(fig_2008)
    if year == 2009:    
        st.write(fig_2009)
    if year == 2010:    
        st.write(fig_2010)
    if year == 2011:    
        st.write(fig_2011)
    if year == 2012:    
        st.write(fig_2012)
    if year == 2013:    
        st.write(fig_2013)
    if year == 2014:    
        st.write(fig_2014)
    if year == 2015:    
        st.write(fig_2015)
    if year == 2016:    
        st.write(fig_2016)
    if year == 2017:    
        st.write(fig_2017)
    if year == 2018:    
        st.write(fig_2018)
    if year == 2019:    
        st.write(fig_2019)
    if year == 2020:    
        st.write(fig_2020)

# Raw data section

if incident_totals_selection == ("State Totals - Raw Data"):
    st.subheader('See raw data for total incidents by state')
    st.caption('(Per capita values are shown per 100,000 people)')
    st.caption('Hint: Once the dataset is selected, click the column name to sort by ascending or descending values')
    with st.expander('click to choose dataset'):
        if st.checkbox('2000'):
            st.write(table_2000)
        if st.checkbox('2001'):
            st.write(table_2001)
        if st.checkbox('2002'):
            st.write(table_2002)
        if st.checkbox('2003'):
            st.write(table_2003)
        if st.checkbox('2004'):
            st.write(table_2004)
        if st.checkbox('2005'):
            st.write(table_2005)
        if st.checkbox('2006'):
            st.write(table_2006)
        if st.checkbox('2007'):
            st.write(table_2007)
        if st.checkbox('2008'):
            st.write(table_2008)
        if st.checkbox('2009'):
            st.write(table_2009)
        if st.checkbox('2010'):
            st.write(table_2010)
        if st.checkbox('2011'):
            st.write(table_2011)
        if st.checkbox('2012'):
            st.write(table_2013)
        if st.checkbox('2014'):
            st.write(table_2014)
        if st.checkbox('2015'):
            st.write(table_2015)
        if st.checkbox('2016'):
            st.write(table_2016)
        if st.checkbox('2017'):
            st.write(table_2017)
        if st.checkbox('2018'):
            st.write(table_2018)
        if st.checkbox('2019'):
            st.write(table_2019)
        if st.checkbox('2020'):
            st.write(table_2020)


if bias_totals_selection == ('Anti-Arab'):
    st.altair_chart(anti_arab)
if bias_totals_selection == ('Anti-Asian'):
    st.altair_chart(anti_asian)
if bias_totals_selection == ('Anti-Atheist or Agnostic'):
    st.altair_chart(anti_atheism_agnosticism)
if bias_totals_selection == ('Anti-Bisexual'):
    st.altair_chart(anti_bisexual)
if bias_totals_selection == ('Anti-Black or African American'):
    st.altair_chart(anti_black_or_african_american)
if bias_totals_selection == ('Anti-Buddhist'):
    st.altair_chart(anti_buddhist)
if bias_totals_selection == ('Anti-Catholic'):
    st.altair_chart(anti_catholic)
if bias_totals_selection == ('Anti-Eastern Orthodox (Russian, Greek, and other)'):
    st.altair_chart(anti_eastern_orthodox_russian_greek_other)
if bias_totals_selection == ('Anti-Female'):
    st.altair_chart(anti_female)
if bias_totals_selection == ('Anti-Gay (male)'):
    st.altair_chart(anti_gay_male)
if bias_totals_selection == ('Anti-Gender Non-Conforming'):
    st.altair_chart(anti_gender_non_conforming)
if bias_totals_selection == ('Anti-Heterosexual'):
    st.altair_chart(anti_heterosexual)
if bias_totals_selection == ('Anti-Hindu'):
    st.altair_chart(anti_hindu)
if bias_totals_selection == ('Anti-Hispanic or Latino'):
    st.altair_chart(anti_hispanic_or_latino)
if bias_totals_selection == ('Anti-Islamic (muslim)'):
    st.altair_chart(anti_islamic_muslim)
if bias_totals_selection == ('Anti-Jehovahs Witness'):
    st.altair_chart(anti_jehovahs_witness)
if bias_totals_selection == ('Anti-Jewish'):
    st.altair_chart(anti_jewish)
if bias_totals_selection == ('Anti-Lesbian (female)'):
    st.altair_chart(anti_lesbian_female)
if bias_totals_selection == ('Anti-Male'):
    st.altair_chart(anti_male)
if bias_totals_selection == ('Anti-Mental Disability'):
    st.altair_chart(anti_mental_disability)
if bias_totals_selection == ('Anti-Mormon'):
    st.altair_chart(anti_mormon)
if bias_totals_selection == ('Anti-Native American'):
    st.altair_chart(anti_american_indian_or_alaska_native)
if bias_totals_selection == ('Anti-Pacific Islander'):
    st.altair_chart(anti_native_hawaiian_or_other_pacific_islander)
if bias_totals_selection == ('Anti-Physical Disability'):
    st.altair_chart(anti_physical_disability)
if bias_totals_selection == ('Anti-Protestant'):
    st.altair_chart(anti_protestant)
if bias_totals_selection == ('Anti-Sikh'):
    st.altair_chart(anti_sikh)
if bias_totals_selection == ('Anti-Transgender'):
    st.altair_chart(anti_transgender)
if bias_totals_selection == ('Anti-White'):
    st.altair_chart(anti_white)
if bias_totals_selection == ('Anti-LGBTQ (grouped)'):
    st.altair_chart(anti_lgbtq_grouped)

