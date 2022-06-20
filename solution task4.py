#!/usr/bin/env python
# coding: utf-8

# ### Sara Magdy Mohamed

# ###  Task4 : Exploratory Data Analysis - Terrorism

# In[169]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')


# In[170]:


terrorism_df= pd.read_csv('globalterrorismdb_0718dist.csv', encoding='latin')
terrorism_df


#    ### Data Exploration

# In[171]:


terrorism_df.columns.values


# In[172]:


# Drop unused columns
df = terrorism_df[['iyear', 'imonth', 'iday','country_txt','region_txt','provstate', 'city', 'latitude', 'longitude','gname',
                   'attacktype1_txt','nkill', 'nwound','target1', 'weaptype1_txt','motive','summary','targtype1_txt' ]]
df.head()


# In[173]:


df.shape


# In[174]:


df.info()


# In[175]:


df.isnull().sum()


# In[176]:


df['nwound']=df['nwound'].fillna(0)
df['nkill']=df['nkill'].fillna(0)


# In[177]:


df['casualties']=df['nwound'] + df['nkill']


# In[178]:


df.info()


# In[179]:


df.describe().round(2)


# In[180]:


df['iyear'].unique()


# In[181]:


df['iyear'].value_counts(dropna=False).sort_index()
plt.figure(figsize = (12,10))
sns.barplot(x = df['iyear'].unique(),y = df['iyear'].value_counts(dropna=False).sort_index(),palette="rainbow")
plt.xticks(rotation = 50)
plt.title('Attacks In Year')
plt.ylabel('No. of attack each years')
plt.xlabel ('Attacks in year')
plt.show()


# In[182]:


# people died due to attacks
df1=df[['iyear','nkill']].groupby(['iyear']).sum()
fig,ax4 =plt.subplots(figsize=(18,10))
df1.plot(kind='bar',alpha=0.8,ax=ax4)
plt.xticks(rotation = 50)
plt.title('people died due to attacks',fontsize=15)
plt.ylabel('No. of killed people',fontsize=20)
plt.xlabel ('year',fontsize=15)
plt.show()


# In[183]:


# top 10 cities effected
df['city'].value_counts().to_frame().sort_values('city', axis=0 , ascending=False).head(10).plot(kind='bar',figsize=(12,8))
plt.xticks(rotation = 50)
plt.title('city')
plt.ylabel('No. of attacks')
plt.xlabel ('top 10 cities effected')
plt.show()


# In[184]:


# top 10 attacktype 
df['attacktype1_txt'].value_counts().head(10).plot(kind='bar',figsize=(12,10))
plt.xticks(rotation = 50)
plt.title('attacktype')
plt.ylabel('No. of attacks')
plt.xlabel ('attacktype ')
plt.show() 


# In[185]:


# number of killed people from each attacktype
df[['attacktype1_txt','nkill']].groupby(['attacktype1_txt']).sum().plot(kind='bar',figsize=(12,8))
plt.xticks(rotation = 90)
plt.title('No. of killed people',fontsize=15)
plt.ylabel('No. of people',fontsize=20)
plt.xlabel ('attack type',fontsize=15)
plt.show()


# In[186]:


# number of wounded people from each attacktype
df[['attacktype1_txt','nwound']].groupby(['attacktype1_txt']).sum().plot(kind='bar',figsize=(12,8))
plt.xticks(rotation = 90)
plt.title('No. of wounded people',fontsize=15)
plt.ylabel('No. of people',fontsize=20)
plt.xlabel ('attack type',fontsize=15)
plt.show()


# In[187]:


df['gname'].value_counts().to_frame().drop('Unknown').head(10).plot(kind='bar',figsize=(12,8))
plt.xticks(rotation = 50)
plt.title('top 10 terrorist group attack')
plt.ylabel('No. of attack')
plt.xlabel ('terrorist group name')
plt.show()


# In[188]:


df[['gname','nkill']].groupby(['gname']).sum().drop('Unknown').sort_values('nkill',ascending= False).head(10).plot(kind='bar',figsize=(12,8))
plt.xticks(rotation = 50)
plt.title('top 10 terrorist group attack')
plt.ylabel('No. of attack')
plt.xlabel ('terrorist group name')
plt.show()


# In[189]:


df[['gname','nkill','country_txt']].groupby(['gname','country_txt']).sum().sort_values('nkill',ascending=False).drop('Unknown').reset_index().head(10)

