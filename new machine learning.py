import numpy as np
import pandas as pd
import pandas as pn
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

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
df = df.drop(['Workclass', 'fnlwgt', 'education', 'marital-status', 'relationship', 'race', 'native-country'], axis= 1)
cols = ["Age", "education-num", "occupation", "sex", "capital-gain", "capital-loss", "hours-per-week", "earnings"]
categorical_features = ["occupation", "sex"]
one_hot = OneHotEncoder()
transformer = ColumnTransformer([("one_hot", one_hot, categorical_features )],remainder="passthrough")
transformed_df = transformer.fit_transform(df)
transformed_df = pd.DataFrame(transformed_df)
transformed_df = transformed_df.head()
print(transformed_df)
