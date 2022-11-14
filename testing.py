import pandas as pd
import numpy as np
import statsmodels.api as sm
import textstat
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\aaron\OneDrive\Documents\quest\test_data.csv")
#df['Organic Searches'].plot.kde()
df['log_organic'] = np.log(df['Organic Searches'] + 1)
# df['log_organic'].plot.kde()
df['question_mark']=0
df['hit'] = df['log_organic'] > 1
print(df['hit'].astype(int))

#df['diversions'] = df['category'].apply(lambda x: 1 if x.contains('diversions') else 0)
df['diversions'] = df['category'].str.contains('diversions')
df['question_mark'] = df['Page Title'].str.contains('\?')
df['date_published'] = pd.to_datetime(df['date_published'])
print(df['date_published'].dt.month)
df['spring_semester'] = ((df['date_published'].dt.month > 1) & (df['date_published'].dt.month < 6))
df['fall_semester'] = ((df['date_published'].dt.month > 8) & (df['date_published'].dt.month < 13))
df['off_season'] = ~(df['fall_semester'] | df['spring_semester'])
df['question_diversions'] = df['diversions'] * df['question_mark']


complexity_list = []
def complexity(df_):
    #complexity_list.append(textstat.flesch_kincaid_grade(df_))
    complexity_list.append(textstat.flesch_reading_ease(df_))
   #complexity_list.append(textstat.smog_index(df_))
df['Page Title'].apply(lambda x: complexity(x))
df['complexity'] = complexity_list

df['complexity'] = ((df['complexity'] >= 50) & (df['complexity'] < 60)).astype(bool)
print(df['complexity'].value_counts())
#rint(complexity_list)

YVar = df[['hit']]
# df['aa'] = np.asarray(df['complexity'])
# df['aa'].to_csv(r"C:\Users\aaron\OneDrive\Documents\quest\aa.csv")
XVar = df[['spring_semester', 'fall_semester', 'off_season', 'complexity']]
# #XVar = sm.add_constant(XVar)
Model = sm.Logit(YVar, XVar).fit()
print(Model.summary())


# df['log_Pageviews'] = np.log(df['Pageviews'] + 1)
# df['hit'] = df['log_Pageviews'] > 2.17

# YVar = df[['hit']]

# Model2 = sm.Logit(YVar, XVar).fit()
# print(Model2.summary())
# df['complexity'] = np.log(df['complexity'] + .1)
# ax = df['complexity'].plot.kde()



#plt.show()
