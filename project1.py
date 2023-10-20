# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 23:32:42 2023

@author: Miguel Silva
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib qt

data = pd.read_csv('C:/Users/Miguel Silva/Desktop/universidade/4th year/1st semester/FAA/Project1/data.csv')
# dropping NaN's only removes 6 observations out 303
data = data.drop(columns="Unnamed: 0").dropna()

# %% SPLITTING LABELS, INTEGER VARIABLES, AND CATEGORICAL VARIABLES

y = data.num.copy();
X = data.drop(columns='num').copy()
X_int = data[['age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'ca']].copy()
X_cat = data[['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'thal']].copy()

# %% NORMALIZATION

def featureNormalization(X):
    mean= np.mean(X, axis=0)
    std= np.std(X, axis=0)
    X_norm= (X-mean)/std
    return X_norm , mean , std

# %% PLOTTING TEST

y = np.array(y)
y = y.reshape([len(y), 1])

#levels of heart disease
zero = (y==0.0)
one = (y==1.0)
two = (y==2.0)
three = (y==3.0)
four = (y==4.0)

x1 = (X_int.age - X_int.age.mean()) / X_int.age.std(); 
x2 = (X_int.trestbps - X_int.trestbps.mean()) / X_int.trestbps.std();
x3 = (X_int.chol - X_int.chol.mean()) / X_int.chol.std();

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x1[zero[:,0]], x2[zero[:,0]], x3[zero[:,0]])
ax.scatter(x1[~zero[:,0]], x2[~zero[:,0]], x3[~zero[:,0]])


# %% DECISION TREE

# after selecting 6 features with spearman correlations inferior to 0.2
# we have: sex, trestbps, chol, fbs, restecg, slope
# let's try for binary: 0 no disease, 1 disease

from sklearn import ensemble
from sklearn.datasets import load_iris
from sklearn import model_selection
from sklearn import metrics
from sklearn import tree

X_filt = X[['sex','trestbps','chol','fbs','restecg','slope']].copy()
X_filt = X_filt.reset_index(drop=True)

y1 = data.num.copy()
y1[y1 != 0] = 1

X_train, X_test, y_train, y_test = model_selection.train_test_split(X_filt, y1, test_size=0.15, random_state=1)

classifier_tree = tree.DecisionTreeClassifier(max_depth=3)
# the max depth of 3 proved to be the optimum
# min_samples_leaf affected negatively accuracy from 40
classifier_tree = classifier_tree.fit(X_train, y_train)
y1_predict = classifier_tree.predict(X_test)

accuracy_tree = metrics.accuracy_score(y_test, y1_predict)

