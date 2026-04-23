import random
import pandas as pd
import numpy as np
import math

def generate_students(n):
    d = []
    for i in range(n):
        rec = (
            i + 1,
            random.randint(40, 100),
            random.randint(60, 100),
            random.randint(10, 30)
        )
        d.append(rec)
    return d

def to_dataframe(d):
    df = pd.DataFrame(d, columns=["id", "marks", "attendance", "assignment"])
    return df

def analyze(df):
    m = df["marks"].values
    a = df["attendance"].values
    ass = df["assignment"].values

    avg_s = (m + a + ass) / 3
    perf_ind = np.sqrt(m * ass)

    df["average"] = avg_s
    df["performance_index"] = perf_ind

    return df

def classify(df):
    categ = []
    for val in df["average"]:
        if val >= 80:
            categ.append("Top Performer")
        elif val >= 60:
            categ.append("Good")
        else:
            categ.append("Average")
    df["category"] = categ
    return df

studs = generate_students(10)
df = to_dataframe(studs)
df = analyze(df)
df = classify(df)

print(df)
print("\nOverall Mean Marks:", np.mean(df["marks"]))
print("Highest Performance Index:", np.max(df["performance_index"]))
print("Log of Average Scores:", [round(math.log(x), 2) for x in df["average"]])