import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Expercise 1 ---------------------------
#Read CSV
df = pd.read_csv('data/fcc-forum-pageviews.csv',parse_dates=['date'])

#Sort again by date
df1 = df.drop(df[(df['value']<df['value'].quantile(0.025)) | (df['value']>df['value'].quantile(0.975))].index)


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
months_2 = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

fig, (ax1, ax2) = plt.subplots(1,2, figsize=(20,8))

plt1 =sns.boxplot(x = "Year", y = "value", data = df3, ax=ax1)
plt1.set_title("Year-wise Box Plot (Trend)")
plt1.set_xlabel('Year')
plt1.set_ylabel('Page Views')

plt2=sns.boxplot(x='Month',y='value',data=df3, ax=ax2)
plt2.set_title("Month-wise Box Plot (Trend)")
plt2.set_xlabel('Month')
plt2.set_ylabel('Page Views')
ax2.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])