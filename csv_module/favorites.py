import csv

with open("favorites.csv") as file:
    reader = csv.DictReader(file)
    counts = {}
    for row in reader:
        if row["language"] in counts:
            counts[row["language"]] += 1
        else:
            counts[row["language"]] = 1
            
for favorite in sorted(counts, key=counts.get, reverse=True):
    print(f"{favorite}: {counts[favorite]}")