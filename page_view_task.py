import numpy as np
import pandas as pd

page_views = pd.read_csv('data/fcc-forum-pageviews.csv',parse_dates=['date'], index_col=['date'])

#page_views.head()
#page_views.info()

#2.5% of smallest and biggest values removed
remove_len = int(round((len(page_views['value'])/100)*2.5,0))
#33 first and last indexes after sorting

sorted_df = page_views.sort_values('value')
#cut first and last 33
sorted_df_removed = sorted_df.iloc[remove_len:len(page_views.sort_values('value'))-remove_len,:]

#sort again by date
page_views_prepared = sorted_df_removed.sort_values('date')