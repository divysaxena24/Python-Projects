trans = [1200, 450, 3000, -50, 50, 2500, 1800, 4000]
 
categories = {
    "normal": [],
    "lrg": [],
    "high_risk": [],
    "invalid": [],
}
 
for amt in trans:
    if amt <= 0:
        categories["invalid"].append(amt)
    elif 1 <= amt <= 500:
        categories["normal"].append(amt)
    elif 501 <= amt <= 2000:
        categories["lrg"].append(amt)
    else:
        categories["high_risk"].append(amt)
 
valid = [amt for amt in trans if amt > 0]
 
total = sum(valid)
count = len(valid)
hr_count = len(categories["high_risk"])
 
if hr_count >= 3:
    level = "High Risk"
elif total > 5000 or count > 5:
    level = "Moderate Risk"
else:
    level = "Low Risk"
 
summary = (total, count, level)
 
print("--- RISK ANALYSIS ---")
print(f"Categories: {categories}")
print(f"Total Value: {summary[0]}")
print(f"Total Transactions: {summary[1]}")
print(f"Final Result: {summary[2]}")
