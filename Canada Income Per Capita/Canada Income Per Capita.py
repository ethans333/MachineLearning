#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model


# In[13]:


df = pd.read_csv("./Data Files/canada_per_capita_income.csv")
df.head()


# In[38]:


reg = linear_model.LinearRegression()
reg.fit(df[["year"]], df["per capita income (US$)"])


# In[39]:


df_income = pd.DataFrame([2020, 2021, 2022, 2023, 2024], columns=["year"])
df_income.insert(1, "per capita income (US$)", reg.predict(df_income))
df_income


# In[46]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.xlabel("year")
plt.ylabel("per capita income (US$)")

plt.scatter(df.iloc[:, 0], df.iloc[:, 1], color='red', marker='.')
plt.scatter(df_income.iloc[:, 0], df_income.iloc[:, 1], color='blue', marker='.')
