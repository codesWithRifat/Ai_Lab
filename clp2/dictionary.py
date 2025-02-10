# Count word occurrences in a given text and store them in a dictionary.
txt = "A kangaroo is really just a rabbit on steroids"
count = {}
words = txt.lower().split()
for i in words:
    i = i.strip()
    if i:
        count[i] = count.get(i, 0) + 1

print(count)
