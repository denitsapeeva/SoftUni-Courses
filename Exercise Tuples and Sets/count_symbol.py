text = input()
counts = {}
for t in text:
    if t not in counts:
        counts[t] = 0
    counts[t] += 1

for key, value in sorted(counts.items()):
    print(f"{key}: {value} time/s")
