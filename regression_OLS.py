import pandas as pd
import statsmodels.api as sm 

df = pd.read_csv(r"C:\Users\aaron\OneDrive\Documents\quest\dbk_consulting\Data for QUEST team Aug. 30, 2020 - Sept. 30 2022.csv")

df = df.iloc[:, 2:]
#df = df.merge(df['category'].str.get_dummies(','), how='left', left_index=True, right_index=True)

df['Page Title'] = df['Page Title'].str.lower()
def addDummy(words):
    for word in words:
        df[word] = df['Page Title'].str.contains(word).astype(int)

addDummy(['umd', 'student', 'dorm', 'covid', 'housing', 'college park', 'review', 'dot'])

X = df.iloc[:, 11:]
y = df['Pageviews'] 
# ## fit a OLS model
X = sm.add_constant(X) 
est = sm.OLS(y, X).fit() 

print(est.summary())

#print()