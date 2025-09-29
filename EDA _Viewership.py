# Databricks notebook source
#install openpyxl in order to manipulate excel file
pip install openpyxl

# COMMAND ----------

#Required after installing openpyxl
%restart_python

# COMMAND ----------

#Importing Libraries
import pandas as pd
import numpy as np

# COMMAND ----------

#Read the excel file
df = pd.read_excel("/Workspace/Users/thatorebecca21@gmail.com/Viewership Analysis - Data.xlsx")

# COMMAND ----------


#View the whole dataset
df

# COMMAND ----------

#View the number of columns and rows of the dataset
df.shape

# COMMAND ----------

#Gives the statistical calculations of the dataset
df.describe()

# COMMAND ----------

#Give out the summary of my dataset
df.info()

# COMMAND ----------

#Calculates the total number of duplicates
df.duplicated().sum()

# COMMAND ----------

#Drop the duplicates and save the changes to original dataset
df.drop_duplicates(inplace=True)



# COMMAND ----------

#Check if there are any duplicates after dropping them
df.duplicated().sum()


# COMMAND ----------

#View the first 5 rows of the dataset
df.head()

# COMMAND ----------

#View the last 5 rows of the dataset

df.tail()

# COMMAND ----------

#View the data types of the columns
df.dtypes

# COMMAND ----------

#Check if there are any null values and calculate the total number of null values
df.isnull().sum()

# COMMAND ----------

#View unique values in the PlayEventType column
df['PlayEventType'].unique()