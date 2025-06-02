import numpy as np
import pandas as pd
netflix=pd.read_csv(r'D:\ScienceD\python practice\elevatesLab_Intern\Task-1\netflix_titles.csv')

#showing the original dataset----------------
print(netflix)

#checking for missing values ------------------
missval=netflix.isnull()
print(missval)
missval=netflix.isnull().sum()
print(missval)

#handling missing values----------
netflix[['director','cast','country']].fillna('unknown')
netflix['date_added'].fillna('00-00-0000')
netflix['rating'].fillna('NR')
netflix['duration'].fillna('0 min')
print("updated data:",netflix)

#fouding duplicates and removing duplicates ----------------
print("Duplicates before removal:", netflix.duplicated().sum()) 
netflix.drop_duplicates(inplace=True)
print("after duplicates removal:", netflix.duplicated().sum())

#standarizing the text values (country)-------------------------------------
netflix['country'] =netflix['country'].str.upper()
print(netflix['country'])

#Convert to datetime (assumes column is called 'date')
netflix['date_added'] = pd.to_datetime(netflix['date_added'], dayfirst=True, errors='coerce')  # 'dayfirst=True' for dd-mm-yyyy
print(netflix['date_added'].head()) #checking the preview

# Clean column names: uppercase, remove spaces
netflix.columns = netflix.columns.str.upper().str.strip().str.replace('_','-')
print(netflix.columns)  # Display cleaned column names

# Check and Fix Data Types
print(netflix.dtypes)

netflix['release_year'] = netflix['release_year'].astype(str)
print(netflix['release_year'].dtypes)  # Check the data type of 'RELEASE-YEAR




