#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import plotly.express as px
import seaborn as sns
import base64


# In[2]:


df = pd.read_csv("E:\internship\grip-tsf\global terrorism excel.csv", low_memory=False, encoding='latin1')
df.head()


# In[3]:


df.info()


# In[4]:


df.columns


# In[5]:


df.describe().T


# In[6]:


df.rename(columns={'iyear': 'Year','imonth':'Month','iday':'Day','city':'City','country_txt':'Country','provstate':'state','region_txt':'Region','attacktype1_txt':'AttackType','target1':'Target','nwound':'Wounded','summary':'Summary','gname':'Group','targtype1_txt':'Target_type','weaptype1_txt':'Weapon_type','motive':'Motive'}, inplace=True)


# In[7]:


df=df[['Year','Month','Day','City','Country','state','Region','AttackType','Target','Wounded','Summary','Group','Target_type','Weapon_type','Motive']]
df.head()


# In[8]:


df.isnull().sum()


# In[9]:


print("Country with the most attacks:",df['Country'].value_counts().idxmax())
print("City with the most attacks:",df['City'].value_counts().index[1]) #as first entry is 'unknown'
print("Region with the most attacks:",df['Region'].value_counts().idxmax())
print("Year with the most attacks:",df['Year'].value_counts().idxmax())
print("Month with the most attacks:",df['Month'].value_counts().idxmax())
print("Group with the most attacks:",df['Group'].value_counts().index[1])
print("Most Attack Types:",df['AttackType'].value_counts().idxmax())


# In[10]:


df.describe()


# In[11]:


df.shape


# In[12]:


df.columns


# In[ ]:


#Number of Attacks


# In[21]:


df['Year'].value_counts(dropna = False).sort_index()


# In[13]:


pd.crosstab(df.Year, df.Region).plot(kind='area',figsize=(15,6))
plt.title('AttackType')
plt.ylabel('Number of Attacks')
plt.show()


# In[ ]:


#Top cities affected


# In[14]:


plt.subplots(figsize=(15,6))
sns.barplot(df['City'].value_counts()[1:15].index,df['City'].value_counts()[1:15].values,palette='inferno')
plt.title('Top Cities Affected')
plt.xlabel('Cities')
plt.ylabel('Count')
plt.xticks(rotation= 90)
plt.show()


# In[ ]:


#Attacking methods


# In[15]:


plt.subplots(figsize=(15,6))
sns.countplot('AttackType',data=df,palette='inferno',order=df['AttackType'].value_counts().index)
plt.xticks(rotation=90)
plt.title('Attacking Methods by Terrorists')
plt.show()


# In[ ]:


#Type of Targets


# In[16]:


plt.subplots(figsize=(15,6))
sns.countplot('Target_type',data=df,palette='inferno',order=df['Target_type'].value_counts().index)
plt.xticks(rotation=90)
plt.title('Type of Target Attacked by Terrorists')
plt.show()


# In[17]:


df["Weapon_type"].value_counts()


# In[ ]:


#methods of Attack


# In[19]:


plt.subplots(figsize=(15,6))
sns.countplot('Weapon_type',data=df,palette='inferno',order=df['Weapon_type'].value_counts().index)
plt.xticks(rotation=90)
plt.title('Type of Weapon Attacked by Terrorists')
plt.show()


# In[ ]:




