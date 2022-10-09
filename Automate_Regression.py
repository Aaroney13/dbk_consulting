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
os.chdir(r"C:\Users\aaron\OneDrive\Documents\quest\dbk_consulting")
df = pd.read_excel(os.getcwd() + '/merged_titles.xlsx')
df = df.drop(df.columns[0], axis=1)
df['date_published'] = pd.to_datetime(df['date_published'])

writer = pd.ExcelWriter(os.getcwd() + '/Top_Headlines/' + 'toplist.xlsx')


# function that produces graphs
# input category and start time and end time frame, save location -> output graph (PNG), list of headlines (CSV) above the line
def regres(start_time, end_time, category, save_location, n, end):
    df2 = df[(df['date_published'] >= start_time) & (df['date_published'] <= end_time)]
    df2 = df2[df2['category'].str.contains(category)]
    date_string = str(start_time)[:10] + '_' + str(end_time)[:10]

    # TESTING AREA
    #if (start_time <= pd.to_datetime('12/31/2019')):
    #x_val = df2['date_published'].values.astype('datetime64[D]').reshape(-1, 1)
    df2['date_published_reg'] = df2['date_published'].map(dt.datetime.toordinal)
    X_val = df2['date_published_reg'].values.reshape(-1, 1)
    Y_val = df2['Organic Searches'].values.reshape(-1, 1)
    ridge = Ridge().fit(X_val, Y_val)
    #print(ridge.predict(X_val))
    reg = LinearRegression().fit(X_val, Y_val)
   # print(df)
    print(reg.coef_)
    #print(df2['date_published'].values.reshape(-1, 1))

    print(len(df2))
    df2['median'] = statistics.median(df2['Organic Searches'])
    #reg.pre
    #df3 = df2[df2['Organic Searches'] > ridge.predict(X_val)]
    df2['predict'] = ridge.predict(X_val).flatten()
    df2['period'] = date_string
    print('end  eee')
    print(n)
    print(end)
    global df3
    df3 = df3.append(df2[df2['Organic Searches'] > df2['predict']])
    if n == 0:
        if end == 0:
            print(df3)
            df3.to_excel(writer,  sheet_name=category, index=False)
    elif n == end:
        df3.to_excel(writer,  sheet_name=category, index=False)
    #print(df3)
    plt.scatter(df2['date_published'], df2['Organic Searches'], alpha=.4)
    plt.title(date_string + ' ' + category)
    plt.xlabel('date')
    plt.ylabel('Organic Searches')
    # plt.plot(df2['date_published'], reg.predict(X_val), color="blue", linewidth=1)
    plt.plot(df2['date_published'], ridge.predict(X_val), color="blue", linewidth=1)
    plt.plot(df2['date_published'], df2['median'], color="red", linewidth=1)
    plt.savefig(os.getcwd() + '/Top_Headlines/' + category + date_string + '.png')
   # plt.show()
    plt.clf()


date_range = pd.date_range(start='12/31/2019', end='8/1/2022', freq='Q')

# TEST DATE
#date_range = [pd.to_datetime(date_range[0]),  pd.to_datetime(date_range[-1])]
end = (len(date_range) - 2)
print(end)

# for loop
# input array of categories and array time frames (pandas datetime objects) to def regres
categories = ['campus', 'news']
for category in categories:
    global df3
    df3 = pd.DataFrame()
    for date_pos in range (0, (len(date_range) - 1)):
        regres(date_range[date_pos], date_range[date_pos + 1], category, 'dbk_consulting/',date_pos, end)
writer.save()
writer.close()