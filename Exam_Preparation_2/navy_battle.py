size = int(input())
matrix = []
my_coordinate = []
lives_of_submarine = 3
battle_cruisers = 0
for row in range(size):
    line = list(input())
    matrix.append(line)
    if "S" in line:
        my_coordinate = [row, line.index("S")]
        matrix[row][my_coordinate[1]] = "-"

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}
while lives_of_submarine > 0 and battle_cruisers < 3:
    command = input()
    row = my_coordinate[0] + directions[command][0]
    col = my_coordinate[1] + directions[command][1]
    my_coordinate = [row, col]
    if matrix[row][col] == "*":
        lives_of_submarine -= 1
        matrix[row][col] = "-"
    elif matrix[row][col] == "C":
        battle_cruisers += 1
        matrix[row][col] = "-"
if battle_cruisers == 3:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
elif lives_of_submarine == 0:
    print(f"Mission failed, U-9 disappeared! Last known coordinates [{my_coordinate[0]}, {my_coordinate[1]}]!")
matrix[my_coordinate[0]][my_coordinate[1]] = "S"
[print(*row,sep="")for row in matrix]