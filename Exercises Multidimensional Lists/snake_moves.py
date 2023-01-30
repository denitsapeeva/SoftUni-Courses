from collections import deque
row, col = (int(x) for x in input().split())
snake = list(input())
snake_copy = deque(snake)

for r in range(row):
    while len(snake_copy) < col:
        snake_copy.extend(snake)


    if r % 2 == 0:
        print(*[snake_copy.popleft()for _ in range(col)], sep="")
    else:
        print(*[snake_copy.popleft() for _ in range(col)][::-1],sep="")
