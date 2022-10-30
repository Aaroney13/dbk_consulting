import pandas as pd
import statsmodels.api as sm 
import matplotlib.pyplot as plt
import os
os.chdir(r"C:\Users\aaron\OneDrive\Documents\quest\dbk_consulting")
df = pd.read_csv(r"C:\Users\aaron\OneDrive\Documents\quest\dbk_consulting\test_data.csv")

df = df.merge(df['category'].str.get_dummies(','), how='left', left_index=True, right_index=True)

df['Page Title'] = df['Page Title'].str.lower()
def addDummy(words):
    for word in words:
        df[word] = df['Page Title'].str.contains(word).astype(int)

addDummy(['umd', 'student', 'dorm', 'covid', 'housing', 'college park', 'review', 'dot'])

# X = df.iloc[:, 11:]
# y = df['Pageviews'] 

# #y = df['Organic Searches']
# # ## fit a OLS model
# X = sm.add_constant(X) 
# est = sm.OLS(y, X).fit() 

corr_matrix = df.corr()
print(corr_matrix)
 
#Using heatmap to visualize the correlation matrix
plt.imshow(corr_matrix)
corr_matrix.to_csv(os.getcwd() + '/matrix.csv')
plt.show()
# print(est.summary())

#print()