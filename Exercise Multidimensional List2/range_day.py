matrix = []
my_position = []
all_targets = 0
targets_hit = 0
indexes_of_shoot_targets = []
for r in range(5):
    matrix.append(input().split())
    if "A" in matrix[r]:
        my_position = [r, matrix[r].index("A")]
    if "x" in matrix[r]:
        all_targets += matrix[r].count("x")

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

for _ in range(int(input())):
    command = input().split()
    if command[0] == "move":
        direction = command[1]
        steps = int(command[2])
        move_row = directions[direction][0]
        move_col = directions[direction][1]
        new_row = my_position[0] + move_row * steps
        new_col = my_position[1] + move_col * steps
        if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix):
            if matrix[new_row][new_col] != "x":
                my_position = [new_row, new_col]
    if command[0] == "shoot":
        direction = command[1]
        shoot_row = directions[direction][0]
        shoot_col = directions[direction][1]
        new_row = my_position[0] + shoot_row
        new_col = my_position[1] + shoot_col
        while 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix):
            if matrix[new_row][new_col] == "x":
                targets_hit += 1
                indexes_of_shoot_targets.append([new_row, new_col])
                matrix[new_row][new_col] = "."
                break
            else:
                new_row += shoot_row
                new_col += shoot_col

    if targets_hit == all_targets:
        print(f"Training completed! All {targets_hit} targets hit.")
        break
if all_targets > targets_hit:
    print(f"Training not completed! {all_targets - targets_hit} targets left.")
for i in range(len(indexes_of_shoot_targets)):
    print(indexes_of_shoot_targets[i])
