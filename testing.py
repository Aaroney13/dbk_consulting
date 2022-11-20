import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
import tensorflow as tf
from tensorflow import keras
from keras.layers import Embedding, SpatialDropout1D, LSTM, concatenate
from keras.layers import Dense
from keras.models import Model
from keras.callbacks import EarlyStopping
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
from keras import Sequential
from sklearn.model_selection import train_test_split
import tensorflow_hub as hub

# ASK ABOUT dates
df = pd.read_csv(r"C:\Users\aaron\OneDrive\Documents\quest\test_data.csv")
#df['Organic Searches'].plot.kde()
avg = df.groupby(by = ['Page Title'], as_index = False).agg({'Pageviews' : 'sum', 'Organic Searches' : 'sum'})
df2 = df.drop_duplicates(subset=['Page Title'])
df = pd.merge(avg, df2[['Page Title', 'date_published', 'category']], how='left', on='Page Title')
df['log_organic'] = np.log(df['Organic Searches'] + 1)

#df['log_organic'] = np.log(df['Organic Searches'] + 1)
# df['log_organic'].plot.kde()
df['question_mark']=0
df['hit'] = df['log_organic'] > 1


df['date_published'] = pd.to_datetime(df['date_published'])
df = df[df['date_published'].dt.year >= 2020]
print(df)
print(len(df))
#print(predictions)
# The maximum number of words to be used. (most frequent)
MAX_NB_WORDS = 50000
# Max number of words in each title
MAX_SEQUENCE_LENGTH = 250 
# This is fixed.
EMBEDDING_DIM = 100
tokenizer = Tokenizer(num_words=MAX_NB_WORDS, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', lower=True)
tokenizer.fit_on_texts(df['Page Title'].values)
word_index = tokenizer.word_index
print('Found %s unique tokens.' % len(word_index))
X = tokenizer.texts_to_sequences(df['Page Title'].values)
X = pad_sequences(X, maxlen=MAX_SEQUENCE_LENGTH)
# print(X)
#X = concatenate([X, df['question_mark'].to_numpy])


print('Shape of data tensor:', X.shape)
y = pd.get_dummies(df['hit'])
Y = y.values

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

model = Sequential()
model.add(Embedding(MAX_NB_WORDS, EMBEDDING_DIM, input_length=X.shape[1]))
print('layer')
model.add(SpatialDropout1D(0.2))
print('layer2')
model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))
print('layer3')
model.add(Dense(2, activation='softmax'))
print('layer4')
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
#model.compile(loss='BinaryCrossentropy', optimizer='adam', metrics=['accuracy'])
print('layer5')
print(X_train.shape,y_train.shape)
print(X_test.shape,y_test.shape)

# set epochs
epochs = 5
batch_size = 64

history = model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size,validation_split=0.1,callbacks=[EarlyStopping(monitor='val_loss', patience=3, min_delta=0.0001)])

accr = model.evaluate(X_test,y_test)
print('Test set\n  Loss: {:0.3f}\n  Accuracy: {:0.3f}'.format(accr[0],accr[1]))
#plt.scatter(predictions.index, predictions)
#plt.show()
#print((y_test.astype(int) - predictions.astype(int)))
#print(predictions)
##print(y_test)
#((y_test - predictions) != 0).to_csv(r"C:\Users\aaron\OneDrive\Documents\quest\predicted_wrong.csv")
# print(df['hit'])
# print(Y)
new_headline = ['umd suffers massive defeat']
seq = tokenizer.texts_to_sequences(new_headline)
padded = pad_sequences(seq, maxlen=MAX_SEQUENCE_LENGTH)
pred = model.predict(padded)
labels = []
print(y.columns)
for val in y.columns:
    if val == True:
        labels.append('not hit')
    else:
        labels.append('hit')
# first represents how much of a hit it is
print(pred, labels[np.argmax(pred)])
print(model.summary())
model.save(r"C:\Users\aaron\OneDrive\Documents\quest\dbk_consulting\model.h5")

# plt.title('Loss')
# plt.plot(history.history['loss'], label='train')
# plt.plot(history.history['val_loss'], label='test')
# plt.legend()
# plt.show()
# plt.title('Accuracy')
# plt.plot(history.history['acc'], label='train')
# plt.plot(history.history['val_acc'], label='test')
# plt.legend()
# plt.show()