from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder

import pandas as pd
import pickle as pk


path = "inputs/trainer.csv"

df = pd.read_csv(path)

Yencoder = OneHotEncoder(sparse_output=False, drop="first")

Y = df.iloc[:, [2]]
Y_ = Yencoder.fit_transform(Y)

with open("raw/y-encoder.pkl", 'wb') as f:
    pk.dump(Yencoder, f)


Xencoder = OneHotEncoder(sparse_output=False, drop='first')

X = df.iloc[:, 3:]
X_ = Xencoder.fit_transform(X)

with open("raw/x-encoder.pkl", 'wb') as f:
    pk.dump(Xencoder, f)


dt = DecisionTreeClassifier()
dt.fit(X_, Y_)

with open("raw/decision-tree.pkl", 'wb') as f:
    pk.dump(dt, f)
