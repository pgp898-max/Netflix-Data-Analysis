import pandas as pd

df = pd.read_csv("netflix_titles.csv")
print(df.head())
df.info()
df.describe()
df.columns
df.isnull().sum()
df['country'].fillna("Unknown", inplace=True)
df['director'].fillna("Unknown", inplace=True)
df['cast'].fillna("Unknown", inplace=True)
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df.drop_duplicates(inplace=True)
df['type'].value_counts()
df['release_year'].value_counts().head(10)
df['country'].value_counts().head(10)
df['listed_in'].str.split(',').explode().value_counts().head(10)
import matplotlib.pyplot as plt
import seaborn as sns
sns.countplot(x='type', data=df)
plt.title("Movies vs TV Shows")
plt.show()
df['country'].value_counts().head(10).plot(kind='bar')
plt.title("Top Countries Producing Content")
plt.show()
df['release_year'].value_counts().sort_index().plot()
plt.title("Content Release Trend")
plt.show()
