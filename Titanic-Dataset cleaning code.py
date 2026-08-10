import pandas as pd

df = pd.read_csv('Titanic-Dataset.csv')


print(df.isnull().sum())
print(f"Duplicates: {df.duplicated().sum()}") 

df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df['Cabin'] = df['Cabin'].fillna('Unknown')

df['Survived'] = df['Survived'].astype(int)

df['Pclass'] = df['Pclass'].astype(int) 
df['Age'] = df['Age'].round(1)
df['Fare'] = df['Fare'].round(2)

df['Ticket'] = df['Ticket'].str.replace(r'\D', '', regex=True)
df['Ticket'] = df['Ticket'].str.replace('.', '')

df.to_csv('Titanic-Cleaned.csv', index=False)
