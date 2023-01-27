def bunny_coordinates(matrix):
    for r in range(len(matrix)):
        for cl in range(len(matrix)):
            if matrix[r][cl] == "B":
                bunny_row = r
                bunny_col = cl
                r = len(matrix)
                return bunny_row, bunny_col


matrix = [list(input().split()) for _ in range(int(input()))]
max_eggs = 0
best_coordinates = []
best_way = ""
bunny_row = 0
bunny_col = 0
directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}
bunny_row, bunny_col = bunny_coordinates(matrix)
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
    if collected_eggs > max_eggs:
        max_eggs = collected_eggs
        best_way = key
        best_coordinates = coordinates
print(best_way)
print(*best_coordinates, sep="\n")
print(max_eggs)



