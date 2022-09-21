import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

df = pd.read_csv(r"C:\Users\aaron\Downloads\Fall 2021 - Spring 2022.csv")

df['date_published'] = pd.to_datetime(df['Page'].str[:11], errors='coerce')

#print(df[df['Page'].str[1:9] == 'category'])

# frpm 72k to 53k observations after getting ones with known published dates
#df[df['date_published'].notnull()]

#df = df[df['date_published'] < dt.datetime(2021, 1, 1)]
# print(df_2020)
# search results and authors are listed as links in title
# 7847 less than 2021, 6215 greater 2021
# print(df)
# print(df[df['Pageviews'] > 2])
print(df['Pageviews'].value_counts())
# plt.scatter(df_2020['date_published'], df_2020['Pageviews'])

# plt.show()

# date range is super important, but some of these titles are in other languages and im not sure

#print(df)
#40k observations published later than 2021