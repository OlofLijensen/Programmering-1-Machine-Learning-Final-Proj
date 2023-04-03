from collections import Counter

import numpy as np


def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))


class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        y_pred = [self._predict(x) for x in X]
        return np.array(y_pred)

    def _predict(self, x):
        # räkna längden
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
        # Sortera distansen
        k_idx = np.argsort(distances)[: self.k]
        # tar fram värdet på y alltså om det är >50k eller <=50K
        k_neighbor_labels = [self.y_train[i] for i in k_idx]
        # ta fram den mest vanliga och ger den nya data punkten de värdet av y
        most_common = Counter(k_neighbor_labels).most_common(1)
        return most_common[0][0]



