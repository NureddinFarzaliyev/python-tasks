import csv
from collections import Counter

with open("favorites.csv") as file:
    reader = csv.DictReader(file)
    counts = Counter()

    for row in reader:
        counts[row["algorithm"]] += 1
            
for favorite, count in counts.most_common():
    print(f"{favorite}: {counts[favorite]}")    