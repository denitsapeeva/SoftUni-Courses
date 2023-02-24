n, m = map(int, input().split())
finish = False
playground = []
player_position = None
opponents_count = 0
for i in range(n):
    row = input().split()
    if 'B' in row:
        player_position = (i, row.index('B'))
    opponents_count += row.count('P')
    playground.append(row)

commands = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

moves_count = 0
touched_count = 0
while True:
    command = input()
    if command == 'Finish':
        finish = True
        break
    row_delta, col_delta = commands[command]
    row, col = player_position[0] + row_delta, player_position[1] + col_delta
    if 0 <= row < n and 0 <= col < m:
        if playground[row][col] == 'P':
            touched_count += 1
            opponents_count -= 1
            moves_count += 1
            playground[row][col] = '-'
            player_position = (row, col)
        elif playground[row][col] != 'O':
            player_position = (row, col)
            moves_count += 1

    if opponents_count == 0:
        print("Game over!")
        print(f"Touched opponents: {touched_count} Moves made: {moves_count}")
        break
if finish:
    print("Game over!")
    print(f"Touched opponents: {touched_count} Moves made: {moves_count}")