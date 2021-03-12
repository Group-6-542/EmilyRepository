#!/usr/bin/env python
# coding: utf-8

# # Merging Group Members' Data
# Emily Stephens (other group members: Jasmine Duong, Lucia Ersfeld, Sarah Siddiqui)
# This tutorial takes four different data sets (number of cultural spaces by zipcode, number of pet licenses per zipcode, number of crimes committed per zipcode, and average income by zipcode) and merges them together. 

# First, import the necessary packages:

# In[2]:


import pandas as pd #for dataframes
import re #for regex


# # Reading in group members' clean and aggregated datasets

# Next, read in the first group member's data. Emily's data lists the number of cultural spaces per Seattle zipcode.

# In[12]:


culturalspacesexcel='https://github.com/elstephens1216/PUBPOL542/blob/main/SeattleAggregatedCulturalSpaces.xlsx?raw=true' #pull in clean data from Github
culturalspaces=pd.read_excel(culturalspacesexcel) #using pandas to create dataframe
culturalspaces #viewing newly created dataframe


# Reading in Lucia's data, which is average income per zipcode, using the same code as above.

# In[6]:


incomeexcel='https://github.com/luciampetersen/PUBPOL542/blob/main/CleanedSeattleIncomeByZip2013.xlsx?raw=true'
income=pd.read_excel(incomeexcel)
income


# Reading in Jasmine's data, which is the number of pet licenses issued per Seattle zipcode. Again, this uses the same code as above.

# In[9]:


petdatacsv='https://github.com/elstephens1216/PUBPOL542/raw/main/jasmineaggpetdata.csv'
petdata=pd.read_csv(petdatacsv)
petdata


# Reading in Sarah's data, which is the number of crimes committed per zipcode in Seattle. This uses the same code as above, as all four datasets are already clean and coming from Github.

# In[6]:


crimecsv='https://github.com/Sarahsid36/SPD/raw/main/SPDdata.csv'
crime=pd.read_csv(crimecsv)
crime


# # Matching data types of merging variable
# Now that all the data has been read in, we need to merge it together, using the key variable zipcode.

# Before merging, we need to make sure the "zipcode" column is being read as the same kind of data type in each of the datasets.

# In[10]:


petdata.dtypes #determining data type of pet data variables


# Note zipcode datatype is int64 (integer) - no action needs to be taken.

# In[13]:


culturalspaces.dtypes


# In[10]:


income.dtypes


# In[8]:


crime.dtypes


# All the "zipcode" columns are being read as int64, so no action needs to be taken. The datasets are now ready to be merged. 

# # Merging data

# Merging Emily's data with Lucia's. By using the command "how='right'", it will only keep rows with a zipcode in the right (i.e., income) dataset. This ensures the merged data doesn't include zipcodes with only partial data.

# In[15]:


project=culturalspaces.merge(income, how='right') #merging two datasets together


# Merging Emily+Lucia with Sarah, using the same code as above.

# In[30]:


project.merge(crime)


# In[16]:


LuciaSarahEmily=project.merge(crime) #renaming merged data


# In[17]:


LuciaSarahEmily #viewing the three merged datasets


# Merging Lucia/Sarah/Emily with Jasmine, the last of the four datasets. This uses the same code as above.

# In[19]:


LuciaSarahEmily.merge(petdata)


# In[20]:


groupdata=LuciaSarahEmily.merge(petdata) #renaming merged data


# In[21]:


groupdata #viewing final merged dataset


# Now that the data has been merged, we need to standardize the column names for ease of analysis in R. To standardize, we chose to make the first word lowercase, and all following words uppercase, for ease of viewing.

# In[23]:


groupdata.columns=['zipcode','culturalSpaces','numberOfReturns','avgAGI','casesReported','numberOfPets'] #renaming columns
groupdata #verifying results


# In verifying the merged data, Rows 24 and 25 are missing data. We want our dataset to include only zipcodes with complete information, so we need to drop rows with missing data.

# In[24]:


groupdata.dropna() #dropping rows with missing data


# In[25]:


groupdata.to_csv(r'C:\Users\elste_000\Documents\mergedGroupDataFinal.csv') #saving final result


# In[ ]:




