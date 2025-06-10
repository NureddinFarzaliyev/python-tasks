from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.DataFrame({
    'age': [20, 12, 50, 43, 23],
    'budget': [2000, 20, 1000, 3400, 5000],
    'buy': ['yes', 'no', 'no', 'yes', 'yes']
})

encoder = LabelEncoder()
df['buy_encoded'] = encoder.fit_transform(df['buy'])

tree = DecisionTreeClassifier()

x = df[['age', 'budget']]
y = df['buy_encoded']

tree.fit(x, y)
tree.predict([[ 20, 2500 ]]) 
