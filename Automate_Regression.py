import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np
import datetime as dt
import os

# Goals
# 1. Automate the regression (organic searches and page views)
# 2. Automate output of 
# - Graphs
# - List of ones above the line
#
os.chdir(r"C:\Users\aaron\OneDrive\Documents\quest\dbk_consulting")
df = pd.read_excel(os.getcwd() + '/merged_titles.xlsx')
df = df.drop(df.columns[0], axis=1)
df['date_published'] = pd.to_datetime(df['date_published'])
print(df)
# function that produces graphs
# input category and start time and end time frame, save location -> output graph (PNG), list of headlines (CSV) above the line
def regres(start_time, end_time, category, save_location):
    df2 = df[(df['date_published'] >= start_time) & (df['date_published'] <= end_time)]
    df2 = df2[df2['category'].str.contains(category)]
    print(len(df2))


date_range = pd.date_range(start='12/31/2019', end='8/1/2022', freq='Q')
print(date_range)
# for loop
# input array of categories and array time frames (pandas datetime objects) to def regres
categories = ['news']
for date_pos in range (0, (len(date_range) - 1)):
  for category in categories:
      regres(date_range[date_pos], date_range[date_pos + 1], category, 'dbk_consulting/')