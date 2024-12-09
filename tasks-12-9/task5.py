words = input("Insert the sentence: ").split(' ')
counts = {}; keys = []

for word in set(words):
    counts[word] = words.count(word)
    keys.append(word)

keys.sort()
for key in keys:
    print(f"{key} {counts[key]}")