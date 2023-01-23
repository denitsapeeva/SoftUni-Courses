rows, columns = [int(x) for x in input().split()]
max_sum = float("-inf")
max_matrix = []
matrix = []
for r in range(rows):
    matrix.append([int(x) for x in input().split()])

for r in range(rows - 2):
    for cl in range(columns - 2):
        first_row = []
        second_row = []
        third_row = []
        for x in range(cl, cl + 3):
            first_row.append(int(matrix[r][x]))
            second_row.append(int(matrix[r + 1][x]))
            third_row.append(int(matrix[r + 2][x]))
        my_sum = sum(first_row) + sum(second_row) + sum(third_row)
        if max_sum < my_sum:
            max_sum = my_sum
            max_matrix.clear()
            max_matrix.append(first_row)
            max_matrix.append(second_row)
            max_matrix.append(third_row)

print(f"Sum = {max_sum}")
[print(*max_matrix[row]) for row in range(len(max_matrix))]
