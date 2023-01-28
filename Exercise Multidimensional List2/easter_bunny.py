size = int(input())
matrix = []
bunny_row = 0
bunny_col = 0
for r in range(size):
    matrix.append(input().split(" "))
    if "B" in matrix[r]:
        bunny_row = r
        bunny_col = matrix[r].index("B")

max_eggs = 0
best_coordinates = []
best_way = ""
directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}
for key, value in directions.items():
    move_row = value[0]
    move_col = value[1]
    collected_eggs = 0
    coordinates = []
    while 0 <= move_row + bunny_row < len(matrix) and 0 <= move_col + bunny_col < len(matrix) and \
            matrix[move_row + bunny_row][move_col + bunny_col] != "X":
        pos_row = bunny_row + move_row
        pos_col = bunny_col + move_col
        collected_eggs += int(matrix[pos_row][pos_col])
        coordinates.append([pos_row, pos_col])
        move_col += value[1]
        move_row += value[0]
    if collected_eggs >= max_eggs:
        max_eggs = collected_eggs
        best_way = key
        best_coordinates = coordinates
print(best_way)
print(*best_coordinates, sep="\n")
print(max_eggs)



