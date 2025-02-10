"""Fill missing values in a dataset with column-wise means."""
import pandas as pd

df = pd.read_csv('data2.csv')
df.fillna(df.mean(numeric_only=True), inplace=True)
print(df)
