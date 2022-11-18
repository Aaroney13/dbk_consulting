import pandas as pd
import statsmodels.api as sm 
import matplotlib.pyplot as plt
import os
os.chdir(r"C:\Users\aaron\OneDrive\Documents\quest\dbk_consulting")
df = pd.read_csv(r"C:\Users\aaron\OneDrive\Documents\quest\dbk_consulting\test_data.csv")

df = df.merge(df['category'].str.get_dummies(','), how='left', left_index=True, right_index=True)

# category
#df = df[df['category'].str.contains('diversions')]

df['Page Title'] = df['Page Title'].str.lower()
def addDummy(words):
    for word in words:
        df[word] = df['Page Title'].str.contains(word).astype(int)

addDummy(['umd', 'student', 'dorm', 'covid', 'housing', 'college park', 'review', 'dot', 'semester', 'basketball', 'win', 'loss'])
df = df.drop(columns=['period', 'residuals'])
df = df[df['Pageviews'] < 200]
df['sum'] = df.iloc[:, -11:].sum(axis=1)

X = df.iloc[:, 11:]
#y = df['Pageviews'] 

y = df['Organic Searches']
# ## fit a OLS model
X = sm.add_constant(X) 
est = sm.OLS(y, X).fit() 

corr_matrix = df.corr()

print(corr_matrix)
#print(corr_matrix.sort_values(by='Organic Searches', ascending=False).head(20))
#Using heatmap to visualize the correlation matrix
plt.imshow(corr_matrix)
#corr_matrix.to_csv(os.getcwd() + '/matrix.csv')
plt.show()
print(est.summary())

