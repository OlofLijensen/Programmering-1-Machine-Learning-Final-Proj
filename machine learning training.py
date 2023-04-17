import numpy as np
import pandas as pn
from sklearn.preprocessing import StandardScaler
from collections import Counter


""" data set Source:
Donor:
Ronny Kohavi and Barry Becker
Data Mining and Visualization
Silicon Graphics.
e-mail: ronnyk '@' live.com for questions. """

cols = ["Age", "Workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-week", "native-country", "earnings"]
df = pn.read_csv("adult.data", names=cols)
df['earnings'] = (df['earnings'] == " >50K").astype(int)

#removing ussless data for knn
df = df.drop(['Workclass', 'education', 'marital-status', 'relationship', 'race', 'native-country','occupation', 'sex'], axis= 1)
np.random.seed(42)


train, valid, test = np.split(df.sample(frac=1), [int(0.6*len(df)), int(0.8*len(df))])

def scale_dataset(dataframe):
    x = dataframe[dataframe.columns[:-1]].values
    y = dataframe[dataframe.columns[-1]].values


    scaler = StandardScaler()
    x = scaler.fit_transform(x)

    data = np.hstack((x, np.reshape(y, (-1, 1))))



    return data, x, y


train, x_train, y_train = scale_dataset(train)
valid, x_valid, y_valid = scale_dataset(valid)
test, x_test, y_test = scale_dataset(test)
def distance(x1, x2):
    distance = np.absolute(x1 - x2)
    return distance



List = []
k = 5
sum = 0
Awnser_list = []
#sorting the x_train rows distance to test dataset so only closest 5 shows in a list as a tuple of "distance" "y" value.
for row in x_test:
    List = []
    flat_list = []
    for (value2, row1) in zip(y_train, x_train):
        sum = 0
        for(value1, value) in zip(row1, row):
            sum += distance(value1, value)

        List.append((sum, value2))
    List.sort(key= lambda item:item[0])
    List = List[:k]
    flat_list = [item for sublist in List for item in sublist]
    most_common = Counter(flat_list).most_common(1)
    Awnser = most_common[0][0]
    Awnser_list.append(Awnser)
print("almost done")

right_counter= 0
for (Awnser_value, y_test_value) in zip (Awnser_list, y_test):
    if Awnser_value == y_test_value:
        right_counter += 1
        print(right_counter)

acc = right_counter/len(y_test)
print(acc)















