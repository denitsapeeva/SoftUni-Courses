rows, columns = [int(x) for x in input().split()]
matrix = []
for r in range(rows):
    matrix.append(input().split())

squares = 0

for r in range(rows-1):
    for cl in range(columns -1):
        target = matrix[r][cl]

        if target == matrix[r][cl +1] and target == matrix[r+1][cl] and target == matrix[r+1][cl+1]:
            squares += 1
            continue
print(squares)

