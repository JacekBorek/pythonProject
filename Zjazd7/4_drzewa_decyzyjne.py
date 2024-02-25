import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from mlxtend.plotting import plot_decision_regions

df = pd.read_csv('iris.csv')

X1 = df[['sepallength','sepalwidth']]
X2 = df[['pedallength','pedalwidth']]
X3 = df.iloc[:,:4]
y = df.class_value

X_train, X_test, y_train, y_test = train_test_split(X1, y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X3, y)

print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))

plot_decision_regions()

