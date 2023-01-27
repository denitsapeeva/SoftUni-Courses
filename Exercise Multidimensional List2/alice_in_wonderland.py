size = int(input())
matrix = []
my_coordinate = []
tea_bags = 0
for row in range(size):
    matrix.append(input().split())
    if "A" in matrix[row]:
        my_coordinate = [row, matrix[row].index("A")]
        matrix[row][my_coordinate[1]] = "*"

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}
while tea_bags < 10:
    command = input()
    row = my_coordinate[0] + directions[command][0]
    col = my_coordinate[1] + directions[command][1]
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        my_coordinate = [row, col]
        step = matrix[row][col]
        matrix[row][col] = "*"
        if step.isdigit():
            tea_bags += int(step)
        elif step == "R":
            break
    else:
        break


if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
for r in range(size):
    print(f"{' '.join(x for x in matrix[r])}")