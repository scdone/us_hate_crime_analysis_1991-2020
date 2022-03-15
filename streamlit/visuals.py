import pandas as pd 
import matplotlib.pypot



df_x = pd.read_csv(rX)
df_x = df_x[['state', 'total_incidents_per_capita']]
df_x.replace(state_dict, inplace=True)
df_x.rename(columns={"state":"State", "total_incidents_per_capita":"Total Hate Crimes Per 100,000 People (x)"}, inplace=True)

fig_x = px.choropleth(df_x, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Total Hate Crimes Per 100,000 People (x)", 
                         color_continuous_scale = "Reds") 

fig_x.show()



map_x = df_x.copy()
map_x.replace(state_dict, inplace=True)
map_x.rename(columns={"state":"State", "total_incidents_per_capita":"Hate Crimes Per Capita"}, inplace=True)

fig_x = px.choropleth(map_x, 
                         locations='State', 
                         locationmode="USA-states", 
                         scope="usa", 
                         color= "Hate Crimes Per Capita", 
                         color_continuous_scale = "YlOrRd")
fig_x.update_layout(title_text='Total Reported Hate Crimes Per Capita Across the U.S. in x')



transposed_x = df_x.transpose()
transposed_x.rename(index={'total_incidents_per_capita':'x'}, inplace=True)
transposed_x.columns = state_list
transposed_x.drop(index=['state'], inplace=True)