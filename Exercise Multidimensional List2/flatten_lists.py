matrix = [x for x in input().split("|")]
new_matrix = []
for el in matrix[::-1]:
    new_matrix.extend(el.split())
print(*new_matrix)