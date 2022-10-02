import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np
import datetime as dt

df = pd.read_csv(r"C:\Users\aaron\Downloads\Fall 2021 - Spring 2022.csv")

df['date_published'] = pd.to_datetime(df['Page'].str[:11], errors='coerce')

categorys = df[df['Page'].str[1:9] == 'category']

# frpm 72k to 53k observations after getting ones with known published dates
df = df[df['date_published'].notnull()]

#df = df[df['date_published'] < dt.datetime(2021, 1, 1)]
# print(df_2020)
# search results and authors are listed as links in title
# 7847 less than 2021, 6215 greater 2021
# print(df)
# print(df[df['Pageviews'] > 2])

# df_2019 = df[(df['date_published'] > dt.datetime(2019, 1, 1)) & (df['date_published'] < dt.datetime(2020, 1, 1))]
# df_2020 = df[(df['date_published'] > dt.datetime(2020, 1, 1)) & (df['date_published'] < dt.datetime(2021, 1, 1))]
#df = df[(df['date_published'] > dt.datetime(2019, 1, 1)) & (df['date_published'] < dt.datetime(2021, 1, 1))]
# df_2022 = df[(df['date_published'] > dt.datetime(2022, 1, 1)) & (df['date_published'] < dt.datetime(2023, 1, 1))]
# print(df_2019['Pageviews'].sum())
df2 = df.sort_values(by=['Pageviews'], ascending=False)
print(len(df2))

df2['cumperc'] = df2['Pageviews'].cumsum()/df2['Pageviews'].sum()*100

df2 = df2.groupby('Page Title')

#print(df2['Pageviews'].sum().sort_values(ascending=False))
#print(df2)
#df2 = df2.drop_duplicates(subset='Page Title', keep='first')


# plt.scatter(df_2020['date_published'], df_2020['Pageviews'])
#df = df.groupby(['Fullname', 'Zip'], as_index=False)['Amount'].sum()


#plt.axis.set_major_formatter(PercentFormatter())

#fig, ax = plt.subplots()

# plot of top headlings ******
# ax.bar(df2.head(20)['Page Title'] , df2.head(20)['Pageviews'], color='k')
# ax.set_facecolor('#f1eeedff')
# fig.set_facecolor('#f1eeedff')

# #add cumulative percentage line to plot
# ax2 = ax.twinx()
# ax2.plot(df2.head(20)['Page Title'], df2.head(20)['cumperc'], color='#4949e7', marker="D")

# ax2.yaxis.set_major_formatter(PercentFormatter())
# ax2.tick_params(axis='y', colors='#4949e7')
# df2['YearMonth'] = df2['date_published'] + pd.offsets.MonthEnd(-1) + pd.offsets.Day(1)

# g = df2.groupby('YearMonth')

# res = g['Pageviews'].sum()

# ax.plot(res.index, res.values)

# print(df2['Pageviews'].value_counts())
df3 = pd.DataFrame(df2.sum(),columns=['Pageviews', 'Organic Searches', 'Users', 'New Users'])
df3 = df3.join(pd.DataFrame(df2.max(),columns=['Avg. Session Duration', 'date_published', 'Page']))
df3.to_excel('c:/Users/aaron/OneDrive/Documents/quest/dbk_consulting/merged_titles.xlsx')

#plt.show()
#fig.savefig('c:/Users/aaron/OneDrive/Documents/quest/dbk_consulting/graph.png', transparent=True, dpi=200)
#plt.show()

# date range is super important, but some of these titles are in other languages and im not sure

#print(df)
#40k observations published later than 2021