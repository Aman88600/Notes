import pandas as pd

df = pd.read_csv("max_true_followers.csv", encoding='utf-8')
column_data = df["Username"].tolist()  # replace "username" with your column name

print(column_data)
