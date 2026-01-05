
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("data/student_scores.csv")


top_index = df["score"].idxmax()
color = ["blue"]*len(df)
color[top_index]="orange"

plt.bar(df["name"], df["score"], color = color)
plt.xlabel("student name")
plt.ylabel("score")
plt.title("Students Scores")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("student_scores.png")
plt.show()
