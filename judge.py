import pickle as pk

import warnings
warnings.filterwarnings("ignore")

with open("raw/y-encoder.pkl", 'rb') as f:
    Yencoder = pk.load(f)

with open("raw/x-encoder.pkl", 'rb') as f:
    Xencoder = pk.load(f)

with open("raw/decision-tree.pkl", 'rb') as f:
    dt = pk.load(f)

while 1:
    st = input("Codes? ").split('\t')

    try:
        r = dt.predict(Xencoder.transform([st]))
        print("\n", Yencoder.inverse_transform([r])[0][0], "\n")
    except:
        if 'y' in input("Error, wanna quit?").lower():
            break

