import pandas as pd
import scipy.stats as stats
import os 
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing
os.chdir(r"C:\Users\aaron\OneDrive\Documents\quest\dbk_consulting")
# Goal: test keywords to see if mean is higher than complement in group
writer = pd.ExcelWriter(os.getcwd() + '/logcheck.xlsx', mode='a', if_sheet_exists='replace')

os.chdir(r"C:\Users\aaron\OneDrive\Documents\quest\dbk_consulting")
df = pd.read_excel(os.getcwd() + '/merged_titles.xlsx', sheet_name='Sheet1')
df = df.drop(df.columns[0], axis=1)
df['Page Title'] = df['Page Title'].str.lower()
df3 = df[df['category'].str.contains('sports')]
df2 = df[~df['category'].str.contains('sports')]

#df['sports'] = df['category'].str.contains('sports')
#df['Organic Searches'] = df['Organic Searches'].apply(lambda x: preprocessing.normalize(x) if x.sports == True)
#df['review'] = df['Page Title'].str.contains('review')
df3['Organic Searches'] = preprocessing.normalize([df3['Organic Searches']]).flatten()
df2['Organic Searches'] = preprocessing.normalize([df2['Organic Searches']]).flatten()
df3['sports'] = True
df2['sports'] = False

df3 = pd.concat([df3, df2])
df3.to_excel(writer,  sheet_name='both', index=False)

writer.save()
writer.close()

word = 'review'
# df = df[df['Organic Searches'] < 2900]
print(df['Organic Searches'].count())
print(df['Organic Searches'].describe())
# doesnt contain word

print(df['Pageviews'][~df['Page Title'].str.contains(word)].describe())

# # contains word
print(df['Pageviews'][df['Page Title'].str.contains(word)].describe())
# print(df['Organic Searches'][df['Page Title'].str.contains(word)])

#print(stats.levene(df['Organic Searches'][~df['Page Title'].str.contains(word)], df['Organic Searches'][df['Page Title'].str.contains(word)], center= 'mean'))