import pandas as pd
import numpy as np
import statsmodels.api as sm
import textstat
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow import keras

model = keras.models.load_model(r"C:\Users\aaron\OneDrive\Documents\quest\saved_model.pb")
