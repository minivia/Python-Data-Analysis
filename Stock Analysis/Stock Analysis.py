#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Importing libraries

from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('whitegrid')
import plotly
import cufflinks as cf
cf.go_offline()


# In[10]:


# Setting start and end parameters

start = datetime.datetime(year=2021,month=1,day=1)
end = datetime.datetime(year = 2022,month=1,day=1)


# In[26]:


#Loading in stock data from Yahoo Finance 

TSLA = data.DataReader('TSLA','yahoo',start,end)

AAPL = data.DataReader('AAPL','yahoo',start,end)

AMZN = data.DataReader('AMZN','yahoo',start,end)

FB = data.DataReader('FB','yahoo',start,end)

SP500 = data.DataReader('^GSPC','yahoo',start,end)

TWTR = data.DataReader('TWTR','yahoo',start,end)


# In[27]:


TSLA.head()


# In[28]:


AAPL.head()


# In[29]:


AMZN.head()


# In[30]:


FB.head()


# In[31]:


SP500.head()


# In[32]:


TWTR.head()


# In[33]:


# Making all stocks into one data frame

tickers = ['AAPL','AMZN','FB','SP500','TSLA','TWTR']
all_stocks = pd.concat([AAPL,AMZN,FB,SP500,TSLA,TWTR],axis=1,keys=tickers)
all_stocks.head()


# In[34]:


all_stocks.columns.names = ['Bank Ticker','Stock Info']


# In[35]:


all_stocks.head()


# In[36]:


# Check for nulls
for col in all_stocks.columns:
    pct_missing = np.mean(all_stocks[col].isnull())
    print('{} - {}%'.format(col,round(pct_missing*100)))


# In[37]:


#Code to Reach Close for Each Stock
close_stock = all_stocks.xs(key='Close',axis=1,level='Stock Info')
# Max for each stock
close_stock.max()


# In[38]:


# Min for each stock
close_stock.min()


# In[39]:


# Date of max for each stock
close_stock.idxmax()


# In[40]:


# Date of min for each stock
close_stock.idxmin()


# In[41]:


# Best months vary, while worst months close in March


# In[42]:


# Create a dataframe for daily returns
returns = pd.DataFrame()


# In[43]:


for tick in tickers:
    returns[tick+' Return'] = all_stocks[tick]['Close'].pct_change()
    
returns.head()


# In[44]:


returns.dropna(inplace=True)
returns.head()


# In[45]:


sns.pairplot(returns)


# In[46]:


# Find lowest days of returns


# In[47]:


returns.idxmin()


# In[48]:


# Find highest days of returns


# In[49]:


returns.idxmax()


# In[50]:


returns.std()


# In[51]:


# Conclusion: Tesla Has Highest Variation, S&P 500 Is Clearly The Least


# In[52]:


## Distribution Plots of Top 3 STD Stock Returns


# In[53]:


sns.displot(returns['FB Return'],color='red',bins=50,kde=True)


# In[56]:


sns.displot(returns['TWTR Return'],color='blue',bins=50,kde=True)


# In[57]:


sns.displot(returns['TSLA Return'],color='green',bins=50,kde=True)


# In[58]:


# Creating Visualizations Based off Closing Prices


# In[59]:


close_stock.plot(figsize=(5,10))


# In[60]:


# Heatmap and Clustermap of Stock Correlations


# In[61]:


# Creating Correlation Matrix based off Closing Price
closing_corr = close_stock.corr()
closing_corr


# In[62]:


sns.heatmap(closing_corr,annot=True,cmap='coolwarm')


# In[63]:


sns.clustermap(closing_corr,annot=True,cmap='coolwarm')


# In[64]:


# Interactive heatmap through plotly that shows correlation and stocks when you hover
closing_corr.iplot(kind='heatmap')


# In[ ]:




