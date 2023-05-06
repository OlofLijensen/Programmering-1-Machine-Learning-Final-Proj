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

# removing ussless data for knn
df = df.drop(['Workclass', 'education', 'marital-status', 'relationship', 'race', 'native-country','occupation', 'sex'], axis= 1)
np.random.seed(42)

# spliting data to train test valid
train, valid, test = np.split(df.sample(frac=1), [int(0.6*len(df)), int(0.8*len(df))])


# Scaling data so big numb dont take over
def scale_dataset(dataframe):
    x = dataframe[dataframe.columns[:-1]].values
    y = dataframe[dataframe.columns[-1]].values


    scaler = StandardScaler()
    x = scaler.fit_transform(x)

    # reformating to ndarray (2 dimensions)
    data = np.hstack((x, np.reshape(y, (-1, 1))))



    return data, x, y


# applying scale to every dataset.
train, x_train, y_train = scale_dataset(train)
valid, x_valid, y_valid = scale_dataset(valid)
test, x_test, y_test = scale_dataset(test)


def Knn(x_train, x_test, y_train, y_test, k):
 def distance(x1, x2):
    distance = np.absolute(x1 - x2)
    return distance

 Awnser_list = []
 # sorting the x_train rows distance to test dataset so only closest 5 shows in a list as a tuple of "distance" "y" value.
 for row in x_test:
    List = []
    for (value2, row1) in zip(y_train, x_train):
        sum = 0
        for(value1, value) in zip(row1, row):
            sum += distance(value1, value)

        List.append((sum, value2))
    List.sort(key= lambda item:item[0])
    List = List[:k]

    # flatning list and using a counter and then using a counter to see if 0 or 1 occurs more often in the flattened list
    flat_list = [item for sublist in List for item in sublist]
    most_common = Counter(flat_list).most_common(1)
    Awnser = most_common[0][0]
    Awnser_list.append(Awnser)
 print("almost done")

 right_counter = 0
 for (Awnser_value, y_test_value) in zip (Awnser_list, y_test):
    if Awnser_value == y_test_value:
        right_counter += 1
        print(right_counter)

 acc = right_counter/len(y_test)


 return acc

def predicter(x_train, x_test, y_train):
 k = 5

 def distance(x1, x2):
  distance = np.absolute(x1 - x2)
  return distance


#sorting the x_train rows distance to test dataset so only closest 5 shows in a list as a tuple of "distance" "y" value.
#this part is just the same as knn i will make this a sepperat funtcion thats why i copyied it from the upper part.
 for row in x_test:
   List = []
   for (value2, row1) in zip(y_train, x_train):
        sum = 0
        for(value1, value) in zip(row1, row):
            sum += distance(value1, value)

        List.append((sum, value2))
   List.sort(key= lambda item:item[0])
   List = List[:k]
   flat_list = [item for sublist in List for item in sublist]

   results = 50000
   Distances_worth = []
   procent_list = []
   changing_list = []
   tot = 0
   x = 0
   y = 1
   zero_count = 0
   one_count = 0

#looping the distances over a exponential funktion to make the closer distances worth more
   for elements in flat_list:
      worth = 1 * 0.9**flat_list[x]
      Distances_worth.append(worth)
      x += 2
      tot += worth
      if x == 10:
          x = 0
          #looping over the new found values and getting them their own percentage of the their own values
          for elements in Distances_worth:
              worth = Distances_worth[x]/tot
              procent_list.append(worth)
              x += 1
              if x == 5:
               x = 0
               #finally cheacking weather the percentage values is attached to a 1 or a 0 aka if the data row is >50K or <=50k.
               #splitting them if their a 1 add 1 to the percentage to get "förändrings faktor" and if their a 0 subbtracted percentage from 1 to get "förändrings faktor"
               #when everything is done get all "förändrings faktor" and times it all with 50.
               #final thing is when the list is all made of mostly made of 0 and 1 the resualts get to big or small thus making it slightly unrealistic.
               #final thing is just a counter capped at max 2 1s or 2 0s and if the loop seas more of the numbers they just skip it.
               for elements in flat_list:
                if x == 5 or y == 11:
                    x = 0
                    y = 0
                    zero_count = 0
                    one_count = 0

                    for value in changing_list:
                        results = results * value
                    print(round(results),"$")
                    changing_list = []

                    break

                elif flat_list[y] == 0:

                 if zero_count == 2:
                    x += 1
                    y += 2


                 else:
                  worth = 1 - procent_list[x]
                  changing_list.append(worth)
                  y += 2
                  x += 1
                  zero_count += 1

                elif flat_list[y] == 1:
                   if one_count == 2:
                    x += 1
                    y += 2

                   else:
                    worth = 1 + procent_list[x]
                    changing_list.append(worth)
                    y += 2
                    x += 1
                    one_count += 1
          break
predicter(x_train, x_test, y_train)








































