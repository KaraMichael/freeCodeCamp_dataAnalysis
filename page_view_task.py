import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Expercise 1 ---------------------------
#Read CSV
page_views_df = pd.read_csv('data/fcc-forum-pageviews.csv',parse_dates=['date'])

#Sorted DF
sorted_df = page_views_df.sort_values('value')

#2.5% of smallest and biggest values
remove_len = int(round((len(page_views_df['value'])/100)*2.5,0))

#Cut first and last 33 (2.5%)
sorted_df_removed = sorted_df.iloc[remove_len:len(page_views_df.sort_values('value'))-remove_len,:]

#Sort again by date
df1 = sorted_df_removed.sort_values('date')

#create figure
fig, axes = plt.subplots()
axes.plot(df1, linestyle='solid')
axes.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
axes.set_xlabel("Date")
axes.set_ylabel("Page Views")

#Expercise 2 ---------------------------
#Get month & year
df2 = df1.copy()
df2['Month'] = pd.DatetimeIndex(df2['date']).month
df2['Year'] = pd.DatetimeIndex(df2['date']).year

#cluster by year and then month
df2 = df2.groupby(['Year', 'Month'])['value'].mean()
df2 = df2.unstack()

#Preprare month
month_names=['January', 'February', 'March', 'April', 'May', 'June', 'July',
             'August', 'September', 'October', 'November', 'December']

#create figure
fig = df2.plot(kind= 'bar', figsize = (15,10)).figure

plt.title('')
plt.xlabel('Years')
plt.ylabel('Average Page Views')
lg = plt.legend(title= 'Months', fontsize = 15, labels = month_names)
title = lg.get_title()
title.set_fontsize(15)

#Expercise 3 ---------------------------
df3 = df1.copy()
df3.reset_index(inplace=True)
df3['Year'] = pd.DatetimeIndex(df3["date"]).year
df3['Month'] = pd.DatetimeIndex(df3["date"]).month

fig, (ax1, ax2) = plt.subplots(1,2, figsize=(20,8))

plt1 =sns.boxplot(x = "Year", y = "value", data = df3, ax=ax1)
plt1.set_title("Year-wise Box Plot (Trend)")
plt1.set_xlabel('Year')
plt1.set_ylabel('Page Views')

plt2=sns.boxplot(x='Month',y='value',data=df3, ax=ax2)
plt2.set_title("Month-wise Box Plot (Trend)")
plt2.set_xlabel('Month')
plt2.set_ylabel('Page Views')