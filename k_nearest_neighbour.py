# -*- coding: utf-8 -*-
"""K Nearest Neighbour

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Lkf_SLWq3--el63_7VjbfcaMgfGz3WYs
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.datasets import load_iris
iris = load_iris()
# %matplotlib inline

iris.feature_names

iris.target_names

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df.head()

df.shape

df['target'] = iris.target
df.head()

df0 = df[:50]
df1 = df[50:100]
df2 = df[100:]

plt.xlabel('Sepal Lenght')
plt.ylabel('Sepal Width')
plt.scatter(df0['sepal length (cm)'], df0['sepal width (cm)'], c='g', marker='+')
plt.scatter(df1['sepal length (cm)'], df1['sepal width (cm)'], c='b', marker='.')

x = df.drop(['target'], axis = 'columns')
y = df.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)

knn.score(x_test, y_test)

y_pred = knn.predict(x_test)
cm = confusion_matrix(y_test, y_pred)
cm