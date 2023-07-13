# Final Project for the Shape AI course in Data Analytics 

![Simple Elegant Graph Facebook Post For Business Coach And Blogger](https://user-images.githubusercontent.com/72509000/123558024-8e5e9300-d76a-11eb-9f05-4ba076ec3887.png)

# Airbnb Rio de Janeiro Data Analysis

![Airbnb Logo](https://www.area360.com.au/wp-content/uploads/2017/09/airbnb-logo.jpg)

[Airbnb](https://www.airbnb.com.br/) is already considered to be the **largest hotel company today**. Oh, the thing is, it **doesn't own any hotels**!

Connecting people who want to travel (and stay) with hosts who want to conveniently rent their properties, Airbnb provides an innovative platform to make this accommodation alternative.

By the end of 2018, the startup, founded 10 years ago, had **hosted more than 300 million** people around the world, challenging traditional hotel chains.

One of Airbnb's initiatives is to make website data available for some of the main cities in the world. Through the [Inside Airbnb](http://insideairbnb.com/get-the-data.html) portal, you can download a large amount of data to develop *Data Science* projects and solutions.

In this *notebook*, we will analyze the data for the city of Rio de Janeiro, and see what insights can be extracted from the raw data.

## Necessary Requirements to Run the Project

* Python 3 installed on your machine.
* Pandas library for data manipulation.
* Matplotlib library for data visualization.
* Seaborn library for statistical data visualization.

You can install the necessary libraries using pip, as follows:

```python
pip install pandas matplotlib seaborn
```
# Logic
The logic of this project is to use the Airbnb dataset to extract insights about the accommodations in Rio de Janeiro. We will use Python along with its libraries to manipulate the data, analyze, and visualize it.

# Procedures for Execution
Clone this repository to your machine.
Navigate to the cloned repository.
Make sure you have all the necessary libraries installed.
Run the Jupyter Notebook.
Data Analysis
The data used in this project is a summary version of the dataset. We will import the necessary packages, load the data into a DataFrame, and then perform exploratory data analysis to understand the structure of the data and extract insights.

```python
# import the necessary packages
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

# import the file listings.csv to a DataFrame
df = pd.read_csv('http://data.insideairbnb.com/brazil/rj/rio-de-janeiro/2021-03-21/visualisations/listings.csv')
```
# Conclusion
In this project, we managed to get some information about Airbnb in the city of Rio de Janeiro. We learned that the data is not always complete. Several values were missing and needed to be cleared as they were outliers, causing our results and outputs to differ greatly from reality before they were addressed. We learned that sometimes the outputs may not represent reality, inducing analyzing data to be distorted producing dubious insights. Although we have a fair amount of insight, this csv used is just a shortened version of the real dataset. To truly explore the data and have the best insights, the ideal would be to use a full version of the csv file, which contains many more variables and attributes.
