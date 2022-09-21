from lib2to3.pgen2.pgen import DFAState
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

df = pd.read_csv(r"C:\Users\aaron\Downloads\Fall 2021 - Spring 2022.csv")

df['date_published'] = pd.to_datetime(df['Page'].str[:11], errors='coerce')

#print(df[df['Page'].str[1:9] == 'category'])

# frpm 72k to 53k observations after getting ones with known published dates
#print(df[df['date_published'].notnull()])

df_2020 = df[df['date_published'] > dt.datetime(2020, 1, 1)]
print(df_2020)
# search results and authors are listed as links in title


plt.scatter(df_2020['date_published'], df_2020['Pageviews'])

plt.show()

# date range is super important, but some of these titles are in other languages and im not sure

#print(df)