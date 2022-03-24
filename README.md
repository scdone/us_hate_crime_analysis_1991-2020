# U.S. Hate Crime Analysis 
### By Stetson Done

## Project Overview

The hate crime data used for this analysis was compiled and provided to the public by the U.S. Federal Bureau of Investigation (FBI).

The FBI considers crimes which are motivated in whole or in part by bias against a race, gender, gender identity, religion, disability, sexual orientation, or ethnicity to be classified as hate crimes. The presence of bias by an offender alone does not constitute a hate crime, as it must be shown through investigation that the particular crime was motivated by said bias.

### Sources:

Data for this analysis was compiled from [FBI U.S. hate crime data](https://crime-data-explorer.fr.cloud.gov/pages/downloads), [U.S. Census data](https://www.census.gov/data.html), and data from the [Pew Research Center](https://www.pewresearch.org/politics/2017/10/24/political-typology-reveals-deep-fissures-on-the-right-and-left/). To see all data wrangling and cleaning efforts, click [here](https://github.com/scdone/us_hate_crime_analysis_1991-2020/tree/main/jupyter_notebooks)

### Limitations:
This data is collected by the FBI through local law enforcement agencies. It must be understood by anyone analyzing or looking at the analysis of the data that the data does not represent law enforcement effectiveness. In addition, different states' local agencies had different levels of participation in the Uniform Crime Report over time, and therefore there may be some inherent exclusions of hate crimes which were not reported by local agencies.

Moreover, it is important to remember that due to the nature of hate crimes, victims are often part of marginalized communities. Therefore, many hate crimes are unreported by the victims due to fear of re-victimization or retaliation. Thus, there may be additional shortcomings from the analysis of the data as a true representation of all hate crime across the United States.


## Dataset Descriptions
>[FBI Hate Crime Dataset](/working_notebooks/dataset_descriptions/hate_crime_dataset_description.ipynb)

<br/>

>[US Census Population Dataset](working_notebooks\dataset_descriptions\population_dataset_description_and_wrangling.ipynb)

## Data Wrangling and Cleaning
>[Wrangling, cleaning, and merging datasets for dataframes](jupyter_notebooks\preparing_dataframe_wrangling_and_cleaning)


## Project Findings & Key Insights
>[see analysis in jupyter notebook here](jupyter_notebooks\analysis\correlation_analysis.ipynb)

>### How are changes in political opinions over time related to trends in hate crimes per capita?")

As I compiled and visualized the data in this project, I wondered what factors may be affecting changes in hate crimes per capita of certain bias categories.

Using data from the Pew Research Center, a research institute which surveys respondents across the U.S. on various topics, I asked the following questions: 

**1. What relationship is there, if any, between the percentage of people who believe homomsexuality should be accepted by society and the amount of anti-gay or anti-lesbian hate crimes per capita?**

**2. What relationship is there, if any, between the percentage of people who support gay and lesbian marriage and the amount of anti-gay or anti-lesbian hate crimes per capita?**

Before we go further, it is important to emphasize correlation does not equal causation. In this analysis, I am looking at relationships bewtween variables but it should not be assumed a causal relationship exists when any amount of correlation is present.

From my analysis, I gained the following insights:

### 1. What relationship is there, if any, between the percentage of people who believe homomsexuality should be accepted by society and the amount of anti-gay or anti-lesbian hate crimes per capita?

The data used for this analysis consisted of total hate crimes per capita in the U.S. which were classified as Anti-Gay (male) or Anti-Lesbian (female), and results from Pew Research Center surveys of the percentage of people who agreed that homosexuality should be accepted by society. Both sets of data spanned from 2000-2020. I chose not to include the grouped LGBTQ hate crimes in this analysis because the question posed was only related to homosexuality, not gender identity or other groups within the LGBTQ+ community. 

First, I ran a pearsonr calculation on the data, which provides a correlation coefficient and a p-value of two data sets. For the correlation coefficient, the closer the number is to -1 or 1, the stronger the correlation. For the p-value, anything under 0.05 is considered to be statistically significant.

For the anti-gay hate crimes, the pearsonr calculation showed a coefficient of -0.5 and p-value of 0.02, which suggests a **moderate negative relationship which is statistically significant.** In other words, as the the percent of people who believed homosexuality should be accepted by society increased, the anti-gay hate crimes per capita decreased. A regression plot of the two variables is shown below:

[image](images\gay_society_regplot.png)

For the anti-lesbian hate crimes, the coefficient and p-value from the pearsonr calculation were -0.8 and -0.00001 respectively, which indicates a **strong negative relationship with high statistical significance.** A regression plot of the two variables is shown below: 

[image](images\lesbian_society_regplot.png)

###  2. What relationship is there, if any, between the percentage of people who support gay and lesbian marriage and the amount of anti-gay or anti-lesbian hate crimes per capita?

Similar to the analysis of the data above, the data used to answer this question was total hate crimes per capita in the U.S. which were classified as Anti-Gay (male) or Anti-Lesbian (female), and results from Pew Research Center surveys of the percentage of people who supported the legality of gay and lesbian marriage.

For the anti-gay data, the coefficient was -0.56 with a p-value of 0.009, which suggests a **moderate negative relationship which is statistically significant**. A scattlerplot of the data is shown below:

[image](images\gay_society_regplot.png)

The anti-lesbian data showed a **strong negative relationship with a high statistical significance** with a coefficient of -0.8 and a p-value of 0.000006. A regression plot of the data is shown below:

[image](images\lesbian_marriage.png)

### Limitations

After looking at these correlations, I decided to do further analysis to check the validity of these correlations. 

When using data over the course of time, it is often useful to take the “first difference” of the data points. To do this, each value subtracts the value directly preceding it from itself. This aims to flatten the trend over time. See example below:


>Line plot of trend over time (percent of people accepting of homosexuality)

[image](images\percent_accepting_with_trend.JPG)
    
>Line plot of "first difference" values (percent of people accepting of homosexuality)

[image](images\percent_accepting_difference.JPG)

>Line plot of trend over time (anti-gay hate crimes per capita)

[image](images\anti_trend_trend.JPG)
    
>Line plot of "first difference" values (anti-gay hate crimes per capita)

[image](images\anti_gay_difference.JPG)  

The reason this is necessary is to see if values are actually correlated to each other (one goes up or down and the other goes up or down in tandem) or if they are both simply correlated to time. 

I chose to try this on the anti-gay hate crimes per capita and the percent of people who thought homosexuality should be accepted by society. When I flattened the trend over time by calculating the correlation of the differences, I found no correlation. 

This could mean a few things. Maybe there is a true correlation, maybe there isn’t. What this analysis really comes down to is I do not currently have enough data to make any objective conclusions. 

Going forward, I would like to collect data exhibiting the population of each demographic over time to find a per capita value which is specific to the particular bias. For example, I currently have per capita values for the amount of anti-gay hate crimes (and many other biases shown on this site) over time based on the entire population, but it would be most useful to find per capita values for anti-gay hate crimes based on only the population of gay men, etc. 

For the time series data, it would also be much more useful to have more than 20 years’ worth of data. 

I plan to continue to find, collect, clean, and analyze more data in this area in the future in order to make more informed conclusions. 

### Future Questions

There are many more questions I would like to analyze in the future upon finding the appropriate data. 
For instance, can anything be identified which could explain the increase of hate crimes across the U.S. over the last six years? In the chart below, we can see the rate of hate crimes per capita has risen every year since 2014, back to levels on par with 2001 (post-9/11).

### U.S. Hate Crimes Per Capita

[image](images\us_total.JPG)

Similarly, I am very interested in what factors might explain this dramatic increase over the past 8 years of anti-transgender hate crimes:

>(Anti-Transgender hate crime was not tracked until 2012, thus the zero values until then. However, every year since anti-transgender crimes have been tracked, they have increased dramatically.)

#### Anti-Transgender Hate Crimes Per Capita

[image](images\anti_transgender_totals.JPG)

### Conclusion

As they say, knowledge is power. As I continue searching for appropriate data to compare with reported hate crimes in the U.S., I hope to find answers to some of these questions. Afterall, if we can identify related social or political factors, we may be on the way to finding factors which could decrease the rate of hate crimes against marginalized communities.


