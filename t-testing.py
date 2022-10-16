import pandas as pd
import scipy.stats as stats
import os 

# Goal: test keywords to see if mean is higher than complement in group

# Check assumptions of t test
# -unequal variances

# perform t test
os.chdir(r"C:\Users\aaron\OneDrive\Documents\quest\dbk_consulting")
df = pd.read_excel(os.getcwd() + '/merged_titles.xlsx')
df = df.drop(df.columns[0], axis=1)
df['Page Title'] = df['Page Title'].str.lower()
df = df[df['category'].str.contains('campus')]
#test = df['Organic Searches'][df['Page Title'].str.contains('umd')]
word = 'art'
print(stats.ttest_ind( df['Organic Searches'][~df['Page Title'].str.contains(word)], df['Organic Searches'][df['Page Title'].str.contains(word)], equal_var=False))

#print(stats.levene(df['Organic Searches'][~df['Page Title'].str.contains(word)], df['Organic Searches'][df['Page Title'].str.contains(word)], center= 'mean'))