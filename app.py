import pandas as pd
import numpy as np
import statsmodels.api as sm
import textstat
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow import keras
from keras.preprocessing.text import Tokenizer



# must change to same dataset as in model
df = pd.read_csv(r"C:\Users\aaron\OneDrive\Documents\quest\test_data.csv")
MAX_NB_WORDS =  50000

model = keras.models.load_model("C:/Users/aaron/OneDrive/Documents/quest/dbk_consulting/saved_model.pb")
MAX_SEQUENCE_LENGTH = 250 
tokenizer = Tokenizer(num_words=MAX_NB_WORDS, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', lower=True)
tokenizer.fit_on_texts(df['Page Title'].values)

new_headline = ['bad headline this is bad headline baddddddddddddddddddd headline']
seq = tokenizer.texts_to_sequences(new_headline)
padded = pad_sequences(seq, maxlen=MAX_SEQUENCE_LENGTH)
pred = model.predict(padded)

pred = model.predict(padded)
print(pred)#, labels[np.argmax(pred)])
