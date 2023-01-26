rows = int(input())
matrix = []
for r in range(rows):
    matrix.append(input().split())
command = input().split()
while True:
    if command[0] == "END":
        break
    row = int(command[1])
    col = int(command[2])
    value = int(command[3])
    if command[0] == "Add":
        if 0 <= row <= len(matrix)-1 and 0 <= col <= len(matrix)-1:
            number = int(matrix[row][col])
            new_number = number+value
            matrix[row][col] = str(new_number)
        else:
            print("Invalid coordinates")
    elif command[0] == "Subtract":
        if 0 <= row <= len(matrix)-1 and 0 <= col <= len(matrix)-1:
            number = int(matrix[row][col])
            new_number = number - value
            matrix[row][col] = str(new_number)
        else:
            print("Invalid coordinates")
    command = input().split()
[print(*matrix[row]) for row in range(len(matrix))]





