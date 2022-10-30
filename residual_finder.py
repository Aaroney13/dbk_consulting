import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import os
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
import statistics
import numpy as np
# Goals
# 1. Find residuals for each article basesd on when it was published
# 2. create new dataset

# Original dataset with headlines and pageviews/organic searches
os.chdir(r"C:\Users\aaron\OneDrive\Documents\quest\dbk_consulting")
global df
df = pd.read_csv(r"C:\Users\aaron\OneDrive\Documents\quest\dbk_consulting\Data for QUEST team Aug. 30, 2020 - Sept. 30 2022.csv")
df['residuals'] = np.nan
df['period'] = np.nan
df = df.iloc[:, 2:]

df['date_published'] = pd.to_datetime(df['date_published'])


# function that produces graphs
# input category and start time and end time frame, save location -> output graph (PNG), list of headlines (CSV) above the line
def regres(start_time, end_time, n, end):
    global df
    df2 = df[(df['date_published'] >= start_time) & (df['date_published'] <= end_time)]

    # Get headlines published within range, date_string = naming schema

    date_string = str(start_time)[:10] + '_' + str(end_time)[:10]

    # Reshaping and fitting data to ridge regression
    df2['date_published_reg'] = df2['date_published'].map(dt.datetime.toordinal)
    X_val = df2['date_published_reg'].values.reshape(-1, 1)
    Y_val = df2['Organic Searches'].values.reshape(-1, 1)
    ridge = Ridge().fit(X_val, Y_val)

    # Linear regression test, to compare with ridge
    reg = LinearRegression().fit(X_val, Y_val)
    print(reg.coef_)

    # Column with predicted regression values
    df2['predict'] = ridge.predict(X_val).flatten()
    df2['residuals'] = df2['predict'] - df2['Organic Searches']

    #df = pd.merge(df, df2[['residuals', 'period']], left_index=True, right_index=True, how='left')
    df['residuals'] = df['residuals'].fillna(df2['residuals'])
  #  print(df)





# Time frame to calculate on
date_range = pd.date_range(start='12/31/2019', end='10/1/2022', freq='Q')
print(date_range)
# TEST DATE
#date_range = [pd.to_datetime(date_range[0]),  pd.to_datetime(date_range[-1])]

# Used to check if last iteration so excel sheet can be written
end = (len(date_range) - 2)
print(end)

u = df.select_dtypes(include=['datetime'])
df['date_published'] = u.fillna(pd.to_datetime('1999-12-31'))
print(date_range)
regres(pd.to_datetime('1998-12-31'), date_range[0], 0, end)

for date_pos in range (0, (len(date_range) - 1)):
    regres(date_range[date_pos], date_range[date_pos + 1], date_pos, end)
df.to_csv(r"C:\Users\aaron\OneDrive\Documents\quest\dbk_consulting\test_data.csv")

