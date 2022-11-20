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

model = keras.models.load_model(r"C:\Users\aaron\OneDrive\Documents\quest\dbk_consulting\model.h5")
MAX_SEQUENCE_LENGTH = 250 
tokenizer = Tokenizer(num_words=MAX_NB_WORDS, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', lower=True)


new_headline = ['titles that have never cant existed']
tokenizer.fit_on_texts(new_headline)
seq = tokenizer.texts_to_sequences(new_headline)
print(seq)
padded = pad_sequences(seq, maxlen=MAX_SEQUENCE_LENGTH)
print(padded)
#pred = model.predict(padded)

#print(pred)
#, labels[np.argmax(pred)])
#accr = model.evaluate(X_test,y_test)
#print('Test set\n  Loss: {:0.3f}\n  Accuracy: {:0.3f}'.format(accr[0],accr[1]))
