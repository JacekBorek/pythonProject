import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression




df = pd.read_csv('weight-height.csv')
print(df.head(3)) #wyświetl 3 pierwsze wersy
print(df.Gender.value_counts()) #wyświetl ilość kobiet i mezczyzn
df.Height *= 2.54
df.Weight /= 2.2

print(f'Po zmianie jednostek \n {df.head(3)}')

sns.histplot(df.query("Gender=='Female'").Weight)
sns.histplot(df.query("Gender=='Male'").Weight)
plt.show()

#zmiana male i female na liczby

df = pd.get_dummies(df)
print(df.head())
#usunięcie kolumny
del (df['Gender_Male'])
print(df.head())