#!/usr/bin/env python
# coding: utf-8

# ![Simple%20Elegant%20Graph%20Facebook%20Post%20For%20Business%20Coach%20And%20Blogger.png](attachment:Simple%20Elegant%20Graph%20Facebook%20Post%20For%20Business%20Coach%20And%20Blogger.png)
[Airbnb](https://www.airbnb.com.br/) is already considered to be the **largest hotel company today**. Oh, the thing is, he **doesn't own any hotels**!

Connecting people who want to travel (and stay) with hosts who want to conveniently rent their properties, Airbnb provides an innovative platform to make this accommodation alternative.

By the end of 2018, Startup, founded 10 years ago, had **hosted more than 300 million** people around the world, challenging traditional hotel chains.

One of Airbnb's initiatives is to make website data available for some of the main cities in the world. Through the [Inside Airbnb](http://insideairbnb.com/get-the-data.html) portal, you can download a large amount of data to develop *Data Science* projects and solutions.

<center><img alt="Analyzing Airbnb" width="10%" src="https://www.area360.com.au/wp-content/uploads/2017/09/airbnb-logo.jpg">< /center>

**In this *notebook*, we will analyze the data for the city of Rio de Janeiro, and see what insights can be extracted from the raw data.**
# ## Rio de Janeiro
# 
# Rio de Janeiro is a Brazilian municipality, capital of the homonymous state, located in the Southeast of the country. The largest international tourist destination in Brazil, Latin America and the entire Southern Hemisphere, the capital of Rio de Janeiro is the best known Brazilian city abroad, functioning as a national "mirror", or "portrait", whether positively or negatively. It is the second largest metropolis in Brazil (after São Paulo), the sixth largest in America and the thirty-fifth in the world. Its population estimated by IBGE for July 1, 2020 was 6 747 815 inhabitants. It has the epithet of Cidade Maravilhosa and the one who is born there is called Carioca.
# 
# It is one of the main economic, cultural and financial centers in the country, being internationally known for several cultural and landscape icons, such as Sugarloaf Mountain, the Corcovado Mountain with the statue of Christ the Redeemer, the beaches of the Copacabana, Ipanema and Barra neighborhoods from Tijuca, among others; the Maracanã and Nilton Santos stadiums; the bohemian neighborhood of Lapa and its arches; the Municipal Theater of Rio de Janeiro; the Tijuca and Pedra Branca forests; Quinta da Boa Vista; the National Library; the island of Paquetá; New Year's Eve in Copacabana; the carioca carnival; Bossa Nova and samba. Part of the city was designated a World Heritage Site by UNESCO on July 1, 2012.
# 
# It represents the second largest GDP in the country (and the 30th largest in the world), estimated at around 329 billion reais (IBGE/2016), and is home to the two largest Brazilian companies - Petrobras and Vale, and the main companies of oil and telephony in Brazil, in addition to the largest conglomerate of media and communications companies in Latin America, Grupo Globo. Contemplated by a large number of universities and institutes, it is the second largest research and development center in Brazil, accounting for 19% of national scientific production, according to 2005 data. Rio de Janeiro is considered a beta global city - according to the 2008 inventory of the Loughborough University (GaWC).
# 
# Consequently, we can agree that taking a trip to Rio de Janeiro wouldn't be bad.

# ## Obtaining the Data
# 
# The data used was obtained from the website [Inside Airbnb](http://insideairbnb.com/get-the-data.html).
# 
# Because this is an initial exploratory analysis, the data used in this project is a summary version of the dataset.

# In[1]:


# import the necessary packages
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# import the file listings.csv to a DataFrame

df = pd.read_csv('http://data.insideairbnb.com/brazil/rj/rio-de-janeiro/2021-03-21/visualisations/listings.csv')


# ## Data analysis
# 
# At this stage, the objective is to ensure an understanding of how the data is structured, so that the reader is aware of what will be analyzed. Therefore, a dictionary will be presented regarding each of the variables.

# **Dictionary of variables**
# 
# * `id` - property identification number
# * `name` - Title of property listing
# * `host_id` - owner identification number
# * `host_name` - hostname
# * `neighbourhood_group` - column with no valid values
# * `neighbourhood` - name of the neighborhood
# * `latitude` - latitude coordinate of the property
# * `longitude` - longitude coordinate of the property
# * `room_type` - type of accommodation offered
# * `price` - rental amount
# * `minimum_nights` - lowest number of nights to rent
# * `number_of_reviews` - ​​number of reviews
# * `last_review` - date of last review
# * `reviews_per_month` - amount of reviews in a month
# * `calculated_host_listings_count` - amount of properties from the same host
# * `availability_365` - number of days of availability within 365 days
# 
# Before we go to the analysis, let's know a little about our *dataset*, taking a look at the first 5 entries.

# In[3]:


# show the first 5 entries
df.head()


# ### **Q1. How many attributes (variables) and how many entries does our dataset have? What types of variables?**
# 
# With a few lines of code, it is possible to notice the presence of 16 variables and 26628 entries, some of which are of types, integer, float, and object.

# In[4]:


# identify DataFrame data volume
print('Entries:\t {}'.format(df.shape[0]))
print('Variables:\t {}'.format(df.shape[1]))
# check the first 5 entries of the dataset
display(df.dtypes)


# ### **Q2. What is the percentage of missing values ​​in the *dataset*?**
# 
# When we look for a *dataset* we want one with quality, it is possible to measure this according to the quantity of missing values. It is necessary to understand whether the null values ​​are significant compared to the total entries.
# 
# * In the column `neighbourhood_group` you can see that 100% of the values ​​were not entered
# * Approximately 37% of the values ​​of `reviews_per_month` and `last_review` variables are null
# * Only 0.1% of the `name` variable values ​​are null

# In[5]:


# sort the variables in descending order by their missing values
(df.isnull().sum() / df.shape[0]).sort_values(ascending = False) 


# In[6]:


# excluding missing values
df.drop(columns=['neighbourhood_group'], inplace=True)
df.dropna(axis=0, inplace=True)

# checking the result
(df.isnull().sum()).sort_values(ascending=False)


# ### **Q3. What is the type of distribution of variables?**
# 
# In order to have a better view of the distribution of variables, I will plot a histogram.

# In[7]:


# plot the histogram of numeric variables
df.hist(bins=15, figsize=(20,15), grid=False);


# ### **Q4. Are there *Outliers* present?**
# 
# If we pay attention to the way in which the histogram is distributing the data, we can find indications of the presence of *outliers*. It is possible to take as an example the variablesprice`price`, `minimum_nights` and `calculated_host_listings_count`.
# 
# Values ​​do not follow a distribution, and distort the graphical representation. To confirm, there are two quick ways to help detect *outliers*. Are they:

# In[8]:


# see summary statistics of numeric variables
df[['price', 'minimum_nights', 'number_of_reviews', 'reviews_per_month',
    'calculated_host_listings_count', 'availability_365']].describe()


# ## Looking at the statistical summary above, we can confirm some hypotheses such as:
# 
# * The `price` variable has 75% of the value below 392, but its maximum value is 129080.
# * The maximum value for the variable (`minimum_nights`) is above 365 days in the year.
# 
# #### **Setting thresholds for 'minimum_nights'**

# In[9]:


q1_minimum_nights = df.minimum_nights.quantile(.25)
q3_minimum_nights = df.minimum_nights.quantile(.75)
IQR_minimum_nights = q3_minimum_nights - q1_minimum_nights
print('IQR da variável minimum_nights: ', IQR_minimum_nights)

# definindo os limites
sup_minimum_nights = q3_minimum_nights + 1.5 * IQR_minimum_nights
inf_minimum_nights = q1_minimum_nights - 1.5 * IQR_minimum_nights

print('Limite superior de minimum_nigths: ', sup_minimum_nights)
print('Limite inferios de minimum_nigths: ', inf_minimum_nights)


# #### **Boxplot para minimum_nights**

# In[10]:


# minimum_nights
df.minimum_nights.plot(kind='box', vert=False, figsize=(15, 3))
plt.show()

# see amount of values ​​above 4.5 days for minimum_nights
print('minimum_nights: valores acima de 4.5:')
print('{} entradas.'.format(len(df[df.minimum_nights > 4.5])))
print('{:.4f}%'.format((len(df[df.minimum_nights > 4.5]) / df.shape[0])*100))


# With that we can extract some information:
# 
# * About 2390 accommodations have a minimum of over 4.5 nights
# * These accommodations represent only 14.7% of the *dataset*

# #### **Setting thresholds for 'Price'**

# In[11]:


# identifying the outliers for the price variable
q1_price = df.price.quantile(.25)
q3_price = df.price.quantile(.75)
IQR_price = q3_price - q1_price
print('IQR of the price variable: ', IQR_price)

# setting the limits
sup_price = q3_price + 1.5 * IQR_price
inf_price = q1_price - 1.5 * IQR_price

print('Upper limit of price: ', sup_price)
print('Lower limit of price: ', inf_price)


# #### **Boxplot for price**

# In[12]:


# price
df.price.plot(kind='box', vert=False, figsize=(15, 3))
plt.show()

# see amount of values ​​above 770 for price
print('\nprice: valores acima de 770')
print('{} entradas'.format(len(df[df.price > 770])))
print('{:.4f}%'.format((len(df[df.price > 770]) / df.shape[0])*100))


# Some insights taken from this analysis:
# 
# * There are approximately 1477 accommodation entries with values ​​above 770 reais.
# * And these accommodations represent only 9.1% of the *dataset*

# #### **Cleaning the dataset**
# 
# After we've identified *outliers* in the `price` and `minimum_nights` variables, let's clean up the *Dataset*.

# In[13]:


# removing *outliers* in a new DataFrame

df_clean = df.copy()
df_clean.drop(df_clean[df_clean.price > 770].index, axis=0, inplace=True)
df_clean.drop(df_clean[df_clean.price == 0.0].index, axis=0, inplace=True)
df_clean.drop(df_clean[df_clean.minimum_nights > 4.5].index, axis=0, inplace=True)

print('Shape before da limpeza: ', df.shape)
print('Shape after da limpeza: ', df_clean.shape)


# #### **Histograms without *outliers***
# 
# With the Dataset clean, I will plot a histogram without the outliers present.

# In[14]:


# plot the histogram for numeric variables
df_clean.hist(bins=15, figsize=(20,15), grid=False);


# In[15]:


# checking the statistical distribution of clean data
df_clean.describe().round(1)


# ### **Q5. What is the average rental price?**
# 
# In an analysis where we have the rent value, it becomes interesting to know the average of this value. In order to take *insights* that help in the calculation of the expense of the accommodation, in a possible trip.
# 
# * It was possible to verify that the *average* rent for the accommodations is **`244.39 reais`**.

# In[16]:


# see the average of the `price` column
df_clean['price'].mean()


# ### **Q6. What is the correlation between the variables?**
# 
# Correlation means that there is a relationship between two things. In the context of analysis, we can look for a relationship or similarity between two variables.
# 
# These relationships can be measured, and it is a function of the relationship coefficient to establish how strong it is. To identify the correlations between the variables of interest, I will:
# 
# * Create a correlation matrix
# * Generate a *heatmap* from this array, using the `seaborn` library
# 

# In[17]:


# create a correlation matrix
corr = df_clean[['price', 'minimum_nights', 'number_of_reviews', 'reviews_per_month', 'calculated_host_listings_count', 'availability_365']].corr()
# show the correlation matrix
display(corr)


# In[18]:


# plot a heatmap from correlations
sns.heatmap(corr, cmap='RdBu' , fmt='.2f', square=True, linecolor='white', annot=True);


# ### **Q7. What is the most rented property type on Airbnb?**
# 
# The `room_type` column indicates which property category is advertised on the platform. On the website, there are options for apartments/entire houses, renting a private room or even sharing the same room with other people.
# 
# Let's count the number of occurrences of each type of rental, using the `value_counts()` method.

# In[19]:


# show the amount of each type of property available
df_clean.room_type.value_counts()


# The types of properties that appear the most are, in order:
# * Entire House/Apt
# * Private rooms
# * Shared rooms
# * Hotel Rooms

# In[20]:


# show the percentage of each type of property available
df_clean.room_type.value_counts() / df.shape[0]


# ##### The properties have a very interesting distribution, see:
# * `Whole houses/apts` and `Private rooms` occupy about 75% of advertised properties
# * And only 1% are `Shared Rooms`

# ### **Q7. What is the most expensive location in Rio de Janeiro?**
# 
# It is possible to check one variable against another using `groupby()`. In this case, we want to compare the neighborhoods (*neighbourhoods*) from the rent price.

# In[21]:


# see prices by neighborhood, on average
df_clean.groupby(['neighbourhood']).price.mean().sort_values(ascending=False)[:10]


# Above we can see that the average values ​​of **Padre Miguel**, **Abolição** and **Sepetiba** are very close, different from other neighborhoods such as **Higienópolis** and **Ipanema**, which have very good values. lower.
# 
# I'm not an expert in Rio de Janeiro so I can't speak properly about the reason for this classification of averages, but it is possible to verify which neighborhoods have more properties advertised, and clarify the doubt if this is due to the amount of properties present in each of the neighborhoods . See below:
# 

# In[22]:


# defining variables to see the amount of properties in each region

pdm = df_clean[df_clean.neighbourhood == 'Padre Miguel'].shape[0]

abl = df_clean[df_clean.neighbourhood == 'Abolição'].shape[0]

spb = df_clean[df_clean.neighbourhood == 'Sepetiba'].shape[0]

lb = df_clean[df_clean.neighbourhood == 'Leblon'].shape[0]

dd = df_clean[df_clean.neighbourhood == 'Deodoro'].shape[0]

abv = df_clean[df_clean.neighbourhood == 'Alto da Boa Vista'].shape[0]

dc = df_clean[df_clean.neighbourhood == 'Del Castilho'].shape[0]

cd = df_clean[df_clean.neighbourhood == 'Cidade de Deus'].shape[0]

ip = df_clean[df_clean.neighbourhood == 'Ipanema'].shape[0]

hi = df_clean[df_clean.neighbourhood == 'Higienópolis'].shape[0]


# Printing the number of properties in each region

print('The number of properties in Padre Miguel is :\t {}'.format(pdm))

print('The number of properties in Abolição is :\t {}'.format(abl))

print('The number of properties in Sepetiba is :\t {}'.format(spb))

print('The number of properties in Leblon is :\t {}'.format(lb))

print('The number of properties in Deodoro is :\t {}'.format(dd))

print('The number of properties in Alto da Boa Vista is :\t {}'.format(abv))

print('The number of properties in Del Castilho is :\t {}'.format(dc))

print('The number of properties in Cidade de Deus is :\t {}'.format(cd))

print('The number of properties in Ipanema is :\t {}'.format(ip))

print('The number of properties in Higienópolis is :\t {}'.format(hi))


# With that we were able to draw some conclusions:
# 
# * The ads with only one property like Padre Miguel, Abolição and Sepetiba are where the most expensive properties are advertised, probably because they only have one property, inflating the price.
# * Although Ipanema has the largest number of ads, it is not the cheapest option, the two properties in Higienópolis are the cheapest alternative. More analysis would be needed to understand this exception that occurs in the Higienópolis neighborhood, analyzing the size of the property or the standard, for example.

# Since Latitudes and Longitudes for properties are provided, it is possible to plot each point. For this, `x=longitude` and `y=latitude` are considered.

# In[23]:


# plot properties by latitude-longitude
df_clean.plot(kind='scatter', x='longitude', y='latitude', alpha=0.4, c=df_clean['price'], s=8,
        cmap=plt.get_cmap('jet'), figsize=(12,8));


# # **Q8. What is the average minimum rental nights (minimum_nights)?**
# 
# We can see that the average minimum number of nights is 2 nights, this shows us that the owners tend to make the properties available for at least 2 nights (weekends)

# In[24]:


# see the average of the `minimum_nights` column

df_clean['minimum_nights'].mean()


# # **Q9. Exploring the most reviewed listings

# In[25]:


# Top 5 most reviewed listings
most_reviewed = df_clean.sort_values(by='number_of_reviews', ascending=False).head()
most_reviewed[['id', 'name', 'number_of_reviews']]


# # **Q10.Exploring the relationship between the price and number of reviews

# In[26]:


# Scatterplot of price vs number_of_reviews
plt.figure(figsize=(10,6))
sns.scatterplot(x='price', y='number_of_reviews', data=df_clean)
plt.title('Price vs Number of Reviews')
plt.xlabel('Price')
plt.ylabel('Number of Reviews')
plt.show()


# # **Q11.Exploring the busiest times of the year

# In[30]:


# Convert last_review to datetime
df_clean['last_review'] = pd.to_datetime(df_clean['last_review'])

# Extract month from last_review and convert it to month name
df_clean['review_month'] = df_clean['last_review'].dt.month_name()

# Count the number of reviews in each month
busy_times = df_clean['review_month'].value_counts()

# Define the correct order of the months
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Reindex the busy_times Series according to the correct order
busy_times = busy_times.reindex(month_order)

busy_times


# # **Q12.Exploring average price by room type

# In[28]:


# Average price by room type
df_clean.groupby('room_type')['price'].mean()


# ## Conclusions
# 
# In this project, we managed to get some information about **Airbnb** in the city of Rio de Janeiro.
# If we consider that the minimum wage in Rio de Janeiro is 1,100 reais, this shows that accommodation is expensive, as the average price is `244.39` reais, which is about 22% of the minimum wage.
# 
# Some other information:
# 
# * About 55% of ads are only for `Whole Houses/Apts`
# * The places with the lowest number of properties advertised are `Padre Miguel`, `Abolição`, `Sepetibal` and `Deodoro`, all with only one property advertised
# * Average `minimum_nights` is approximately 2 nights, probably for guests to rent for at least a weekend (Saturday and Sunday).
# 
# Upon completing this project, we learned that the data is not always complete. Several values ​​were missing and needed to be cleared as they were outliers, causing our results and outputs to differ greatly from reality before they were addressed.
# We learned that sometimes the outputs may not represent reality, inducing analyzing data to be distorted producing dubious insights.
# Although we have a fair amount of insight, this `csv` used is just a shortened version of the real dataset. To truly explore the data and have the best insights, the ideal would be to use a full version of the `csv` file, which contains many more variables and attributes.
