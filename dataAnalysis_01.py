import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
#import sys

#Gives memory size of for example integer in bytes
#sys.getsizeof(5)

#Read csv and show structure
#sales = pd.read_csv('data/sales_data.csv',parse_dates=['Date'])
#conn = sqlite3.connect('data/sakila.db')

df = pd.read_sql('''
    SELECT
        rental.rental_id, rental.rental_date, rental.return_date,
        customer.last_name AS customer_lastname,
        store.store_id,
        city.city AS rental_store_city,
        film.title AS film_title, film.rental_duration AS film_rental_duration,
        film.rental_rate AS film_rental_rate, film.replacement_cost AS film_replacement_cost,
        film.rating AS film_rating
    FROM rental
    INNER JOIN customer ON rental.customer_id == customer.customer_id
    INNER JOIN inventory ON rental.inventory_id == inventory.inventory_id
    INNER JOIN store ON inventory.store_id == store.store_id
    INNER JOIN address ON store.address_id == address.address_id
    INNER JOIN city ON address.city_id == city.city_id
    INNER JOIN film ON inventory.film_id == film.film_id
    ;
''', conn, index_col='rental_id', parse_dates=['rental_date', 'return_date'])

print(df.head())
#sales.head()
#sales.shape
#sales.info()

#Simple and quick analysis
#sales['Customer_Age'].mean()
#sales['Order_Quantity'].mean()
#sales['Year'].value_counts()
#Which country has the most sales quantity of sales?
#sales['Country'].value_counts().head(1)

#Pie Plot
#sales['Year'].value_counts().plot(kind='pie', figsize=(6,6))
#Density Plot
#sales['Customer_Age'].plot(kind='kde', figsize=(14,6))
#Boxplot
#sales['Customer_Age'].plot(kind='box', vert=False, figsize=(14,6))
#Histogram
#sales['Order_Quantity'].plot(kind='hist', bins=30, figsize=(14,6))


#NUMPY

#Create Array raging from 1 to 8
np.arange(1,9)

#Create Array raging from 8 to 1 (can also be done for a matrix)
np.flip(np.arange(1,9))
np.flip(np.matrix(np.arange(1,9)).reshape(2,4))
np.flip(np.matrix(np.arange(1,9)).reshape(2,4), axis=1) #only flip colums

#Create an 2x4 Matrix
df_m = np.matrix(np.arange(1,9)).reshape(2,4)

#Transpose = 2x4 -> 4x2
df_m.transpose()

#Flatten a multidimensional array
df_m.flatten()

#Boolean arrays
df_m <= 2 #Returns array full of boolean
df_m[df_m <= 2] #Returns values which match condition
