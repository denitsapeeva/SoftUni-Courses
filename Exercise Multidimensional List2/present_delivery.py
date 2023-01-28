def cookie(row, col, presents_left):
    good_kids = 0
    bad_kids = 0
    for key, value in directions.items():
        move_row = row + value[0]
        move_col = col + value[1]
        if 0 <= move_row < size and 0 <= move_col < size:
            if neighborhood[move_row][move_col] == "X":
                neighborhood[move_row][move_col] = "-"
                bad_kids += 1
                presents_left -= 1
            elif neighborhood[move_row][move_col] == "V":
                neighborhood[move_row][move_col] = "-"
                good_kids += 1
                presents_left -= 1
        if not presents_left:
            break

    return good_kids, presents_left


all_presents = int(input())
size = int(input())
neighborhood = []
presents_for_nice_kid = 0
presents_left = all_presents
all_nice_kids = 0
santa_coordinates = []
for r in range(size):
    neighborhood.append(input().split())
    if "S" in neighborhood[r]:
        santa_coordinates = [r, neighborhood[r].index("S")]
        neighborhood[r][santa_coordinates[1]] = "-"
    if "V" in neighborhood[r]:
        all_nice_kids += neighborhood[r].count("V")
directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}
command = input()
while command != "Christmas morning":
    new_row = santa_coordinates[0] + directions[command][0]
    new_col = santa_coordinates[1] + directions[command][1]
    if 0 <= new_row < size and 0 <= new_col < size:
        if neighborhood[new_row][new_col] == "V":
            presents_left -= 1
            presents_for_nice_kid += 1
            neighborhood[new_row][new_col] = "-"
            santa_coordinates = [new_row, new_col]
        elif neighborhood[new_row][new_col] == "C":
            neighborhood[new_row][new_col] = "-"
            good, presents_left = cookie(new_row, new_col, presents_left)
            presents_for_nice_kid += good
            santa_coordinates = [new_row, new_col]
        elif neighborhood[new_row][new_col] == "X":
            neighborhood[new_row][new_col] = "-"
            santa_coordinates = [new_row, new_col]
        elif neighborhood[new_row][new_col] == "-":
            santa_coordinates = [new_row, new_col]

    if not presents_left or all_nice_kids == presents_for_nice_kid:
        break
    command = input()
neighborhood[santa_coordinates[0]][santa_coordinates[1]] = "S"
if not presents_left and presents_for_nice_kid< all_nice_kids:
    print("Santa ran out of presents!")
for r in range(size):
    print(f"{' '.join(x for x in neighborhood[r])}")
if presents_for_nice_kid == all_nice_kids:
    print(f"Good job, Santa! {all_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {all_nice_kids - presents_for_nice_kid} nice kid/s.")
