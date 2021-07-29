import csv
from collections import Counter

with open("D:/archive/SOCR-HeightWeight.csv",newline='') as f:
    r = csv.reader(f)
    df = list(r)

df.pop(0)

data = []

for i in range(len(df)):
    h = df[i][1]
    data.append(float(h))

# mean
n = len(data)

total = 0
for j in data:
    total += j

mean = total/n
print(mean)

# median
sortvar = data.sort()
if n%2 == 0 :
    median1 = float(data[n//2])
    median2 = float(data[n//2-1])
    median = (median1 + median2)/2
else:
    median = data[n//2]

print(median)
    
# mode
data1 = Counter(data)
moderange = {"50-60":0,"60-70":0,"70-80":0}
for height,occ in data1.items():
    if 50 < float(height) < 60:
        moderange["50-60"] += occ
    elif 60 < float(height) < 70:
        moderange["60-70"] += occ
    elif 70 < float(height) < 80:
        moderange["70-80"] += occ

mode_range,mode_occurence = 0,0

for range, occurence in moderange.items():
    if occurence > mode_occurence:
         mode_range, mode_occurence = [int(range.split("-")[0]),int(range.split("-")[1])],occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"Mode is -> {mode:2f}")
