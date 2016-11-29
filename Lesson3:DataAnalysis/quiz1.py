import numpy as np
import pandas
import matplotlib.pyplot as plt
import pandasql

def entries_histogram(turnstile_weather):
    '''
    Before we perform any analysis, it might be useful to take a
    look at the data we're hoping to analyze. More specifically, let's 
    examine the hourly entries in our NYC subway data and determine what
    distribution the data follows. This data is stored in a dataframe
    called turnstile_weather under the ['ENTRIESn_hourly'] column.
    
    Let's plot two histograms on the same axes to show hourly
    entries when raining vs. when not raining. Here's an example on how
    to plot histograms with pandas and matplotlib:
    turnstile_weather['column_to_graph'].hist()
    
    Your histogram may look similar to bar graph in the instructor notes below.
    
    You can read a bit about using matplotlib and pandas to plot histograms here:
    http://pandas.pydata.org/pandas-docs/stable/visualization.html#histograms
    
    You can see the information contained within the turnstile weather data here:
    https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/turnstile_data_master_with_weather.csv
    '''

    
    rainquery = "select ENTRIESn_hourly as raining from turnstile_weather where rain = 1 group by Hour "
    rain_entry = pandasql.sqldf(rainquery.lower(), locals())
    
    norainquery = "select ENTRIESn_hourly as noraining from turnstile_weather where rain = 0 group by Hour "
    norain_entry = pandasql.sqldf(norainquery.lower(), locals())

    plt.figure()
    
    
    norain_entry.hist(alpha=0.5)
    rain_entry.hist( alpha=0.5)
    
    
    return plt

