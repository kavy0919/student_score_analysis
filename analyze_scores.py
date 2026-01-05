import pandas as pd

df = pd.read_csv("data/student_scores.csv")

print(df)

average = df["score"].mean()
highest = df.loc[df["score"].idxmax()]
lowest = df.loc[df["score"].idxmin()]
print("average :", average)
print("highest:", highest["name"], highest["score"])
print("lowest:", lowest["name"], lowest["score"])