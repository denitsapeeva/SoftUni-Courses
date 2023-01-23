rows,columns = [int(x) for x in input().split()]
first = ord("a")
matrix = []

for r in range(rows):
    matrix.append([])
    for cl in range(columns):
        matrix[r].append(chr(first)+chr(first+cl)+chr(first))
    first +=1

[print(*matrix[rows]) for rows in range(len(matrix))]
