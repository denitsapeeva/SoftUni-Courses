rows = int(input())
matrix = [list(input())for _ in range(rows)]
positions = (
    (-2, -1),  # top left
    (-2, 1),  # top right
    (-1, -2),
    (-1, 2),
    (2, -1),
    (2, 1),
    (1, -2),
    (1, 2),
)
remove_knights = 0
while True:
    indexes_of_knight_max_attacks = []
    number_of_max_attacks = 0
    for r in range(len(matrix)):
        for cl in range(len(matrix)):
            if matrix[r][cl] == "K":
                attacks = 0
                for pos in positions:
                    pos_row = r + pos[0]
                    pos_col = cl + pos[1]
                    if 0 <= pos_row < rows and 0 <= pos_col < rows:
                        if matrix[pos_row][pos_col] == "K":
                            attacks += 1
                if attacks > number_of_max_attacks:
                    number_of_max_attacks = attacks
                    indexes_of_knight_max_attacks = [r, cl]
    if indexes_of_knight_max_attacks:
        row = indexes_of_knight_max_attacks[0]
        col = indexes_of_knight_max_attacks[1]
        matrix[row][col] = "0"
        remove_knights += 1
    else:
        break
print(remove_knights)




