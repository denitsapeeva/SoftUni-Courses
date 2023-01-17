rows = int(input())
odd_set = set()
even_set = set()
for i in range(1, rows + 1):
    name_len = sum(ord(l) for l in input()) // i
    if name_len % 2 == 0:
        even_set.add(name_len)
    else:
        odd_set.add(name_len)
if sum(odd_set) == sum(even_set):
    print(*odd_set.union(even_set), sep=", ")
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=", ")
else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")
