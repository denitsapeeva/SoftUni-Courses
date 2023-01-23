def check_valid_indexes(indexes):
    if {indexes[0], indexes[2]}.issubset(valid_rows) and {indexes[1], indexes[3]}.issubset(valid_colums):
        return True
    return False


def swap_indexes(command, indexes):
    if check_valid_indexes(indexes) and command == "swap" and len(indexes) == 4:
        row1, col1, row2, cow2 = indexes
        matrix[row1][col1], matrix[row2][cow2] = matrix[row2][cow2], matrix[row1][col1]
        [print(*matrix[row]) for row in range(len(matrix))]
    else:
        print("Invalid input!")


rows, columns = [int(x) for x in input().split()]
matrix = []
for r in range(rows):
    matrix.append([x for x in input().split()])
valid_rows = range(rows)
valid_colums = range(columns)
while True:
    command, *info = [int(x) if x.isdigit() else x for x in input().split()]
    if command == "END":
        break
    swap_indexes(command,info)
