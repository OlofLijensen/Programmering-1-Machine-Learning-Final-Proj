import numpy as np
import pandas as pd
import pandas as pn
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler


""" data set Source:
Donor:
Ronny Kohavi and Barry Becker
Data Mining and Visualization
Silicon Graphics.
e-mail: ronnyk '@' live.com for questions. """

cols = ["Age", "Workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-week", "native-country", "earnings"]
df = pn.read_csv("adult.data", names=cols)
df['earnings'] = (df['earnings'] == " >50K").astype(int)
df = df.drop(['Workclass', 'fnlwgt', 'education', 'marital-status', 'relationship', 'race', 'native-country'], axis= 1)
cols = ["Age", "education-num", "occupation", "sex", "capital-gain", "capital-loss", "hours-per-week", "earnings"]
categorical_features = ["occupation", "sex"]
one_hot = OneHotEncoder()
transformer = ColumnTransformer([("one_hot", one_hot, categorical_features )],remainder="passthrough")
df = transformer.fit_transform(df)
df = pd.DataFrame(df)
print(df)

train, valid, test = np.split(df.sample(frac=1), [int(0.6*len(df)), int(0.8*len(df))])

def scale_dataset(dataframe, oversampler=False):
    x = dataframe[dataframe.columns[:-1]].values
    y = dataframe[dataframe.columns[-1]].values

    scaler = StandardScaler()
    x = scaler.fit_transform(x)

    data = np.hstack((x, np.reshape(y, (-1, 1))))


    if oversampler:
        ros = RandomOverSampler()
        x, y = ros.fit_resample(x, y)


    return data, x, y


train, x_train, y_train = scale_dataset(train, oversampler=True)
valid, x_valid, y_valid = scale_dataset(valid, oversampler=False)
test, x_test, y_test = scale_dataset(test, oversampler=False)
print(len(y_train))
print(len(x_train))


from Knn import KNN
clf = KNN(k=3)
clf.fit(x_train, y_train)
predictions = clf.predict(x_test)

acc = np.sum(predictions == y_test)/len(y_test)

print(acc)



