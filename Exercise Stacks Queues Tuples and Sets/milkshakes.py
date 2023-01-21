from collections import deque

chocolates = deque([int(x) for x in input().split(", ")])
cup_of_milk = deque([int(x) for x in input().split(", ")])
milkshakes = 0

while milkshakes < 5 and chocolates and cup_of_milk:
    current_chocolate = chocolates.pop()
    current_milk = cup_of_milk.popleft()
    if current_milk <= 0:
        chocolates.append(current_chocolate)
        continue
    elif current_chocolate <= 0:
        cup_of_milk.appendleft(current_milk)
        continue

    if current_milk == current_chocolate:
        milkshakes += 1
    else:
        cup_of_milk.append(current_milk)
        chocolates.appendleft(current_chocolate + 5)
if milkshakes >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
print(f"Chocolate: {', '.join(str(x) for x in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in cup_of_milk) or 'empty'}")
