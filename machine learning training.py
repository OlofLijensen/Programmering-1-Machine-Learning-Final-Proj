import numpy as np
import pandas as pn
from sklearn.preprocessing import StandardScaler

import plotly.express as px
import plotly.graph_objects as po
import plotly.io as pio

import seaborn as sea
import matplotlib.pyplot as map

""" data set Source:
Donor:

Ronny Kohavi and Barry Becker
Data Mining and Visualization
Silicon Graphics.
e-mail: ronnyk '@' live.com for questions. """
cols = ["Age", "Workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-week", "native-country", "earnings"]
df = pn.read_csv("adult.data", names = cols)
df['earnings'] = (df['earnings'] == " >50K").astype(int)

train, valid, test = np.split(df.sample(frac=1), [int(0.6*len(df)), int(0.8*len(df))])

def scale_dataset(dataframe):
    x = dataframe[dataframe.cols[:-1]].values
    y = dataframe[dataframe.cols[-1]].values

    scaler = StandardScaler()
    x = scaler.fit_transform(x)

    data = np.hstack((x, np.reshape(y, (-1, 1))))

    return data, x , y

print(len(train[train["earnings"]==1]))
print(len(train[train["earnings"]==1]))