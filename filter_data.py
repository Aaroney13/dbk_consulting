import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np
import datetime as dt

df = pd.read_csv(r"C:\Users\aaron\OneDrive\Documents\quest\dbk_consulting\Data for QUEST team Aug. 30, 2020 - Sept. 30 2022.csv")
print(df)

#df['date_published'] = pd.to_datetime(df['Page'].str[:11], errors='coerce')
#df.to_csv(r"C:\Users\aaron\OneDrive\Documents\quest\dbk_consulting\Data for QUEST team Aug. 30, 2020 - Sept. 30 2022.csv")


# df = df[df['date_published'].notnull()]

# df = df.groupby()
# avg_sal = df.groupby(by = ['Page Title'], as_index = False).agg({'Pageviews' : 'sum', 'Organic Searches' : 'sum'})

# categories = pd.read_csv(r"C:\Users\aaron\OneDrive\Documents\quest\dbk_consulting\Fall 2021 - Spring 2023 Data bad.csv")
# categories = categories[['Page Title', 'category']]
# categories = categories.drop_duplicates(subset='Page Title')
# print(len(df3))
# df3 = pd.merge(df3, categories, on='Page Title', how='left')
# print(len(df3))

# df3 = df3[(df3['Pageviews'] > 50)]#& (df3['Avg. Session Duration'] > 0)]
# print(len(df3))
# df3 = df3[df3['category'].notnull()]
# print(len(df3))

