import pandas as pd
import os

# Goal: Count occurances of keywords and test if higher instancces of keywords mean higher views/searches

xls = pd.ExcelFile(r"C:\Users\aaron\OneDrive\Documents\quest\dbk_consulting\Top_Headlines\toplist.xlsx")

# input categories to test on
categories = ['campus']#, 'diversions', 'news']
# input keywords to test on
keywords = ['umd', 'community']

for category in categories:
    df1 = pd.read_excel(xls, category)
    df1['Page Title'] = df1['Page Title'].str.lower()
    df1['Keywords_count'] = 0
    for keyword in keywords:
        df1['Keywords_count'] = df1['Keywords_count'] + df1['Page Title'].str.count(keyword)
    print(df1['Keywords_count'])