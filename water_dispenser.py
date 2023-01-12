from _collections import deque

dispenser = int(input())
names = deque()

while True:
    my_names = input()
    if my_names == "Start":
        break
    else:
        names.append(my_names)
while True:
    my_input = input()
    if my_input.startswith('refill'):
        litters = my_input.split(" ")
        dispenser += int(litters[1])
    elif my_input == "End":
        print(f'{dispenser} liters left')
        break
    else:
        if dispenser >= int(my_input):
            print(f'{names.popleft()} got water')
            dispenser -= int(my_input)
        else:
            print(f'{names.popleft()} must wait')
