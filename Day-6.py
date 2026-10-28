
text = input("Sentence: ").lower().split()

count = {}
for w in text:
    count[w] = count.get(w, 0) + 1

print(count)
