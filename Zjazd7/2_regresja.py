import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv('otodom.csv')
print(df.head(10).to_string())
# print(df.describe().T.to_string())

# print(df.iloc[2:7,0:4])

#korelacja

#print(df.iloc[:,1:].corr())
# sns.heatmap(df.iloc[:,1:].corr(), annot=True)
# plt.show()
sns.displot(df.cena)
plt.show()

_min = df.describe().loc['min','cena']
q1 = df.describe().loc['25%','cena']
q3 = df.describe().loc['75%','cena']
print(_min, q1, q3)
df1 = df[(df.cena >= q1) & (df.cena <= q3)]
sns.displot(df1.cena)
plt.show()

X = df1.iloc[:, 2:] #wszystkie kolumny prócz ceny
y = df1.cena

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

