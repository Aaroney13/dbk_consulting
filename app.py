import pandas as pd
import numpy as np
import statsmodels.api as sm
import textstat
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow import keras
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
import h5py as h5

MAX_NB_WORDS =  50000

model = keras.models.load_model(r"C:\Users\aaron\OneDrive\Documents\quest\dbk_consulting\new_model.h5")
MAX_SEQUENCE_LENGTH = 250 
tokenizer = Tokenizer(num_words=MAX_NB_WORDS, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', lower=True)

# # CLEANING STEPS *************
# df = pd.read_csv("/content/test_data.csv")
# #df['Organic Searches'].plot.kde()
# avg = df.groupby(by = ['Page Title'], as_index = False).agg({'Pageviews' : 'sum', 'Organic Searches' : 'sum'})
# df2 = df.drop_duplicates(subset=['Page Title'])
# df = pd.merge(avg, df2[['Page Title', 'date_published', 'category']], how='left', on='Page Title')
# df['log_organic'] = np.log(df['Organic Searches'] + 1)


# df['date_published'] = pd.to_datetime(df['date_published'])
# df = df[(df['date_published'].dt.year >= 2020) | df['hit']]
df= pd.read_csv(r"C:\Users\aaron\OneDrive\Documents\quest\filtered_data.csv")
# *********
tokenizer.fit_on_texts(df['Page Title'].values)
new_headline = ["l bozo"]

seq = tokenizer.texts_to_sequences(new_headline)
print(seq)
padded = pad_sequences(seq, maxlen=MAX_SEQUENCE_LENGTH)
print(padded)
pred = model.predict(padded)

#print(pred, labels[np.argmax(pred)])
x = np.arange (0, 1, .1)
print(pred)
#print(nonesense[0][0])
print(pred[0][1])
#plt.plot(nonesense[0][0], 0, 'x', color='b')
plt.plot(pred[0][1], 0, 'x', color='r')
plt.xticks(x)
plt.show()

#, labels[np.argmax(pred)])
#accr = model.evaluate(X_test,y_test)
#print('Test set\n  Loss: {:0.3f}\n  Accuracy: {:0.3f}'.format(accr[0],accr[1]))
