import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.externals import joblib

filename = 'KNN.sav'
loaded_model = joblib.load(filename)
dataset = pd.read_csv('check.csv')
result = loaded_model.predict(dataset)
p = result[0]

p = open("Result.txt", "w")
p.write(str(p))
