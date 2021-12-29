import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#Read CSV
page_views_df = pd.read_csv('data/fcc-forum-pageviews.csv',parse_dates=['date'], index_col=['date'])

#Sorted DF
sorted_df = page_views_df.sort_values('value')

#2.5% of smallest and biggest values
remove_len = int(round((len(page_views_df['value'])/100)*2.5,0))

#Cut first and last 33 (2.5%)
sorted_df_removed = sorted_df.iloc[remove_len:len(page_views_df.sort_values('value'))-remove_len,:]

#Sort again by date
page_views_prepared = sorted_df_removed.sort_values('date')

#create figure
fig, axes = plt.subplots()
axes.plot(page_views_prepared, linestyle='solid')
axes.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
axes.set_xlabel("Date")
axes.set_ylabel("Page Views")
plt.show()