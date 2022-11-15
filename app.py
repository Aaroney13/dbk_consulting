import pandas as pd
import numpy as np
import statsmodels.api as sm
import textstat
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# model building - maybe add to a function so user can upload a new dataset to train on
df = pd.read_csv(r"C:\Users\aaron\OneDrive\Documents\quest\test_data.csv")
df['log_organic'] = np.log(df['Organic Searches'] + 1)
df['hit'] = df['log_organic'] > 1


df['diversions'] = df['category'].str.contains('diversions')
df['question_mark'] = df['Page Title'].str.contains('\?')

df['date_published'] = pd.to_datetime(df['date_published'])
#df = df[df['date_published'].dt.year >= 2020]

df['spring_semester'] = ((df['date_published'].dt.month > 1) & (df['date_published'].dt.month < 6))
df['fall_semester'] = ((df['date_published'].dt.month > 8) & (df['date_published'].dt.month < 13))
df['off_season'] = ~(df['fall_semester'] | df['spring_semester'])
df['question_diversions'] = df['diversions'] * df['question_mark']


complexity_list = []
def complexity(df_):
    #complexity_list.append(textstat.flesch_kincaid_grade(df_))
    complexity_list.append(textstat.flesch_reading_ease(df_))
    return df_
   #complexity_list.append(textstat.smog_index(df_))
df['Page Title'].apply(lambda x: complexity(x))
df['complexity'] = complexity_list

df['complexity_hard'] = (df['complexity'] <= 60).astype(bool)
df['complexity_easy'] = (df['complexity'] >= 70).astype(bool)

df['complexity_standard'] = ((df['complexity'] >= 60) & (df['complexity'] < 70)).astype(bool)
df['complexity_easy'] = ((df['complexity'] >= 70) & (df['complexity'] < 80)).astype(bool)
df['complex_spring_standard'] = df['complexity_standard'] & df['spring_semester']
df['complex_fall_standard'] = df['complexity_standard'] & df['fall_semester']
df['complex_spring_easy'] = df['complexity_easy'] & df['spring_semester']
df['complex_fall_easy'] = df['complexity_easy'] & df['fall_semester']
df['complex_off_standard'] = df['complexity_standard'] & df['off_season']
df['complex_off_easy'] = df['complexity_easy'] & df['off_season']
df['contain_review'] = df['Page Title'].str.contains('Review', case=False)
df['contain_sga'] = df['Page Title'].str.contains('SGA', case=False)
df['contain_umd'] = df['Page Title'].str.contains('UMD', case=False)
df['contain_num'] = df['Page Title'].str.contains('\d+')
print(df['contain_umd'])
#rint(complexity_list)

YVar = df[['hit']]
# df['aa'] = np.asarray(df['complexity'])
# df['aa'].to_csv(r"C:\Users\aaron\OneDrive\Documents\quest\aa.csv")
XVar = df[['spring_semester', 'fall_semester', 'complex_off_standard', 'question_mark', 'contain_review',  'complexity_hard', 'contain_umd', 'complex_fall_easy', 'complex_spring_easy']]

X_train, X_test, y_train, y_test = train_test_split(XVar, YVar, test_size=0.2)

#print(df[['Organic Searches', 'spring_semester', 'fall_semester', 'off_season', 'complexity', 'complex_spring', 'complex_fall']].corr())
# #XVar = sm.add_constant(XVar)
print(y_train)
#Model = sm.Logit(YVar, XVar).fit()
Model = sm.Logit(y_train, X_train).fit()

predictions = Model.predict(X_test)

predictions_to_int = predictions.apply(lambda x: 1 if x > .6 else 0)


((y_test.astype(int)['hit'] - predictions_to_int) == 0)
correct = ((y_test.astype(int)['hit'] - predictions_to_int) == 0).value_counts().iloc[0]
incorrect = ((y_test.astype(int)['hit'] - predictions_to_int) == 0).value_counts().iloc[1]

# beginning of webapp

# function, takes user input returns if its a hit or not
def prediction(input):
    # model predict must take a dataframe but user input could be put into df here
    predict = Model.predict(input)
    # change based on input
    input_to_int = predict.apply(lambda x: 1 if x > .6 else 0)
    return input_to_int


# insert app visualizations
# Use app GUI, try and make sure it could be run in a notebook for them
# they should be able to put in new training data so long as it fits format
print(predictions)

# things to print in app
print(Model.summary())
print('predicted ' + str(correct) + ' correctly and ' + str(incorrect) + ' incorrectly ' + 'this represents a ' + str(correct/len(y_test)) + ' success rate')

print(((y_test.astype(int)['hit'] - predictions_to_int) != 0).where(((y_test.astype(int)['hit'] - predictions_to_int) != 0)).dropna().index)

# add graphs in app