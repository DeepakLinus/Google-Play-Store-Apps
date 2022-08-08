#A
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
#B
!pip install missingno
import missingno as mis
#C
! pip install opendatasets --quiet
import opendatasets as od 
od.download('https://www.kaggle.com/datasets/gauthamp10/google-playstore-apps/download?datasetVersionNumber=7')
#D
data = pd.read_csv('/content/google-playstore-apps/Google-Playstore.csv')
#E
data.head(10)
#F
data.columns
#G
data.shape
#H
data.info()
#I
data.isnull()
#J
data.isnull().sum()
#H
data.isnull().sum().sort_values(ascending = False)
#I
data['Category'].value_counts()
#J
data.describe()
#K
data.columns
#L
data.rename(lambda x: x.lower().strip().replace(' ', '_'), 
            axis='columns', inplace=True)
# Specify the cols to drop
to_drop = [
    'app_id', 'minimum_android', 
    'developer_id', 'developer_website', 'developer_email', 'privacy_policy', 
    'ad_supported', 'in_app_purchases', 'editors_choice'
]

# Drop them
data.drop(to_drop, axis='columns', inplace=True)
#Check:
data.columns
#M
# Collapse 'Music' and 'Music & Audio' into 'Music'
data['category'] = data['category'].str.replace('Music & Audio', 'Music')
# Collapse 'Educational' and 'Education' into 'Education'
data['category'] = data['category'].str.replace('Educational', 'Education')
#Check:
data['category'].value_counts()
#N
top_10_list = [
    'Education', 'Music', 'Tools','Business','Entertainment',  
     'Lifestyle', 'Books & Reference','Health & Fitness','Shopping','Food & Drink',  
]

top = data[data['category'].isin(top_10_list)].reset_index(drop=True)
#Chack:
top['category'].value_counts()
#O
top['released'] = pd.to_datetime(top['released'], format='%b %d, %Y',
                                 infer_datetime_format=True, errors='coerce')
#Check:
top.released.dtype
#P
top['size'] = pd.to_numeric(top['size'].str.replace(r'[a-zA-Z]+', ''), 
                             errors='coerce')
#Q
 top['size'].dtype == 'float64'
#R
mis.matrix(top.sort_values('category'))
#S
mis.heatmap(top, cmap='rainbow')
#T
plt.figure(figsize=(20,7))
plt.title("A Histogram of App ratings")
sns.histplot(top['rating'],kde=True,bins=20)
#U
plt.figure(figsize=(20,7))
plt.title("A Histogram of App ratings")
sns.histplot(top[top['rating']>0]['rating'],bins=20)
#V
plt.figure(figsize=(20,9))
plt.xticks(rotation=90)
plt.xlabel("Highest Rated Category")
plt.ylabel("Number of applications")
plt.title("All Categories Rating ")
sns.barplot(data['category'], data['rating'])
#W
plt.figure(figsize=(20,7))
plt.title("Proportion of 10 Categories")
plt.xlabel("Proportion")
top['category'].value_counts(normalize=True).plot.barh()
#X
plt.figure(figsize=(20,7))
plt.title("Proportion of install categories")
plt.xlabel("Proportion")
top.installs.value_counts(normalize=True).plot.barh()
#Y
with pd.option_context('float_format', '{:f}'.format):
  print(top.rating_count.describe())
#z
plt.figure(figsize=(20,7))
plt.title("Histogram of Rating Count")
plt.xlabel("Ratings")
plt.ylabel('Count')
rating=top[top['rating_count'] < 32]
sns.histplot(rating['rating_count'],bins=20)
#1A
is_paid = top['price'] != 0
with pd.option_context('float_format', '{:f}'.format):
    print(top[is_paid]['price'].describe())
#1B
plt.figure(figsize=(20,7))
plt.title("Free and Paid Apps in Category")
plt.xlabel("Price ($)")
plt.ylabel('$P(X = x)$')
less_15=top[(top['price']>0)&(top['price']<15)]
sns.histplot(less_15['price'],bins=20)
