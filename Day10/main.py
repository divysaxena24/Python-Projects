import random
import copy
import math
import numpy as np
import pandas as pd

def generate_data():
    data = []
    for i in range(12):
        student = {
            "id": i + 1,
            "marks": random.randint(40, 100),
            "attendance": random.randint(60, 100),
            "scores": [random.randint(10, 25), random.randint(10, 25)]
        }
        data.append(student)
    return data

def mutate_data(data):
    for i in range(len(data)):
        data[i]["marks"] = data[i]["marks"] + math.sqrt(data[i]["marks"])
        data[i]["scores"][0] += 5
        data[i]["attendance"] -= 2

def to_dataframe(data):
    flat = []
    for d in data:
        flat.append({
            "id": d["id"],
            "marks": d["marks"],
            "attendance": d["attendance"],
            "internal": d["scores"][0],
            "assignment": d["scores"][1]
        })
    return pd.DataFrame(flat)

def analyze(original, modified):
    orig_marks = np.array([d["marks"] for d in original])
    mod_marks = np.array([d["marks"] for d in modified])

    mean = np.mean(mod_marks)
    median = np.median(mod_marks)
    std = np.std(mod_marks)

    drift = abs(np.mean(orig_marks) - mean)

    manual_mean = sum(mod_marks) / len(mod_marks)

    norm = (mod_marks - np.min(mod_marks)) / (np.max(mod_marks) - np.min(mod_marks))

    return mean, median, std, drift, manual_mean, norm

def classify(drift, threshold, original, shallow):
    if original != shallow:
        return "Copy Failure Detected"
    elif drift < threshold:
        return "Stable Data"
    elif drift < threshold * 2:
        return "Minor Drift"
    else:
        return "Critical Drift"

data = generate_data()

shallow = data.copy()
deep = copy.deepcopy(data)

mutate_data(shallow)
mutate_data(deep)

df_original = to_dataframe(data)
df_shallow = to_dataframe(shallow)
df_deep = to_dataframe(deep)

mean, median, std, drift, manual_mean, norm = analyze(data, deep)

threshold = 5

result = classify(drift, threshold, data, shallow)

print("Original DataFrame:\n", df_original)
print("\nShallow Copy:\n", df_shallow)
print("\nDeep Copy:\n", df_deep)

print("\nDrift:", drift)
print("\nTuple:", (mean, drift, std))
print("\nClassification:", result)
print("\nManual Mean:", manual_mean)
print("\nNormalized Marks:", norm)