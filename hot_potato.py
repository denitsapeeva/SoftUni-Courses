from _collections import deque

all_kids = input().split(" ")
potato_count = int(input())
while len(all_kids) > 1:
    for i in range(potato_count):
        if i < potato_count-1:
            kid_stays = all_kids.pop(0)
            all_kids.append(kid_stays)
        else:
            print(f'Removed {all_kids.pop(0)}')
print(f'Last is {all_kids[0]}')

