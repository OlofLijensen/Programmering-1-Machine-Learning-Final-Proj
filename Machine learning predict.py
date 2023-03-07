import numpy as np
import pandas as pn

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
cols = ["Age", "Workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-week", "native-country", "earnings'"]
df = pn.read_csv("adult.data", names = cols)
df = df.head()


print(df.to_string())



