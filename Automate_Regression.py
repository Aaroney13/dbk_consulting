import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import os
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
import statistics

# Goals
# 1. Automate the regression (organic searches and page views)
# 2. Automate output of 
# - Graphs
# - List of ones above the line
#

# Original dataset with headlines and pageviews/organic searches
os.chdir(r"C:\Users\aaron\OneDrive\Documents\quest\dbk_consulting")
df = pd.read_excel(os.getcwd() + '/merged_titles.xlsx')
df = df.drop(df.columns[0], axis=1)
df['date_published'] = pd.to_datetime(df['date_published'])

# Writer for graphs
writer = pd.ExcelWriter(os.getcwd() + '/Top_Headlines/' + 'toplist.xlsx', mode='a', if_sheet_exists='replace')

# function that produces graphs
# input category and start time and end time frame, save location -> output graph (PNG), list of headlines (CSV) above the line
def regres(start_time, end_time, category, n, end):

    # Get headlines published within range, date_string = naming schema
    df2 = df[(df['date_published'] >= start_time) & (df['date_published'] <= end_time)]
    df2 = df2[df2['category'].str.contains(category)]
    date_string = str(start_time)[:10] + '_' + str(end_time)[:10]

    # Reshaping and fitting data to ridge regression
    df2['date_published_reg'] = df2['date_published'].map(dt.datetime.toordinal)
    X_val = df2['date_published_reg'].values.reshape(-1, 1)
    Y_val = df2['Organic Searches'].values.reshape(-1, 1)
    ridge = Ridge().fit(X_val, Y_val)

    # Linear regression test, to compare with ridge
    reg = LinearRegression().fit(X_val, Y_val)
    print(reg.coef_)

    # Static median to show on graph
    df2['median'] = statistics.median(df2['Organic Searches'])

    # Column with predicted regression values
    df2['predict'] = ridge.predict(X_val).flatten()
    df2['period'] = date_string
    print(n)
    print(end)

    # Global dataframe for each category, later written to excel for each sheet
    global df3
    df3 = df3.concat(df2[df2['Organic Searches'] > df2['predict']])
    if n == 0:
        if end == 0:
            print(df3)
            df3.to_excel(writer,  sheet_name=category, index=False)
    elif n == end:
        df3.to_excel(writer,  sheet_name=category, index=False)

    # graph creation
    plt.scatter(df2['date_published'], df2['Organic Searches'], alpha=.4)
    plt.title(date_string + ' ' + category)
    plt.xlabel('date')
    plt.ylabel('Organic Searches')
    plt.plot(df2['date_published'], ridge.predict(X_val), color="blue", linewidth=1, label='predicted')
    plt.plot(df2['date_published'], df2['median'], color="red", linewidth=1, label='median')
    plt.legend()
    plt.savefig(os.getcwd() + '/Top_Headlines/' + category + date_string + '.png')
   # plt.show()
    plt.clf()

# Time frame to calculate on
date_range = pd.date_range(start='12/31/2019', end='8/1/2022', freq='Q')

# TEST DATE
#date_range = [pd.to_datetime(date_range[0]),  pd.to_datetime(date_range[-1])]

# Used to check if last iteration so excel sheet can be written
end = (len(date_range) - 2)
print(end)

# for loop
# Input array of categories and array time frames (pandas datetime objects) to regres
# Calls regres function on all date ranges for each category
categories = ['diversions']#, 'news']
for category in categories:
    global df3
    df3 = pd.DataFrame()
    for date_pos in range (0, (len(date_range) - 1)):
        regres(date_range[date_pos], date_range[date_pos + 1], category, date_pos, end)

# Saving list excel writer
writer.save()
writer.close()