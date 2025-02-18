#!/usr/bin/env python
# coding: utf-8

# Advanced Use Case: Looping Through a Pandas DataFrame

# In[2]:


import pandas as pd


# In[3]:


data = {
    "Customer": ["Alice","Bob","Charlie","Dacid","Eve"],
    "Amount": [2500, 150, 3200, 500, 1000],
    "Status": ["Completed", "Pending","Completed","Failed","Completed"]
}

df = pd.DataFrame(data)
print(df)


# Looping Through Rows Using iterrows()

# Use iterrows() for simpler row-wise iteration.
# 
# Use filtering (df[df["Column"] == value]) for efficient row selection
# 
# Use apply() for vectorized operations instead of loops (faster)

# In[5]:


for index, row in df.iterrows():
    print(f"Customer: {row['Customer']}, Amount: {row['Amount']}, Status: {row['Status']}")


# Filtering Completed Transactions

# In[6]:


completed_df = df[df["Status"] == "Completed"]

for index, row in completed_df.iterrows():
    print(f"Completed Transaction: {row['Customer']} paid {row['Amount']}")    


# Calculating Total Amount of Completed Transactions

# In[7]:


total_completed_amount = df[df["Status"] == "Completed"]["Amount"].sum()
print(f"Total Amount from completed Transactions: {total_completed_amount}")


# Counting Completed Transactions

# In[8]:


count_completed = df[df["Status"] == "Completed"].shape[0]
print(f"Total Completed Transactions: {count_completed}")


# Using apply() Instead of Loops 

# In[10]:


df["Discounted Amount"] = df["Amount"].apply(lambda x: x * 0.1)
print(df)

