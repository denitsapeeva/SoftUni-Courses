from _collections import deque

my_people = deque()
while True:
    my_input = input()
    if my_input == "Paid":
        while my_people:
            print(my_people.popleft())
    elif my_input == "End":
        break
    else:
        my_people.append(my_input)
print(f"{len(my_people)} people remaining.")
