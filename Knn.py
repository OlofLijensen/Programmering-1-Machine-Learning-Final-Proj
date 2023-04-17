import numpy as np

list1 = np.array([[1, 2, 3], [4, 5, 6]])
list2 = np.array([[7, 8, 9], [10, 11, 12], [13, 14, 15]])
list3 = np.array([1, 0, 1])
def disntance(x1, x2):
    sum = np.absolute(x1 - x2)
    return sum
sum = 0

List = []
for row1 in list1:
    List = []
    for (row2, value3) in zip(list2, list3):
        sum = 0
        for (value1, value2) in zip(row1, row2):
            print(value1,value2,value3)
            sum += disntance(value1, value2)
        List.append((sum,value3))
    print(List)

