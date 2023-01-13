quantity_of_food = int(input())
orders = [int(x) for x in input().split(" ")]
print(max(orders))
while orders:
    if orders[0] <= quantity_of_food:
        quantity_of_food -= orders.pop(0)
    else:
        break

if orders:
    print(f"Orders left: {' '.join([str(x) for x in orders])}")
else:
    print("Orders complete")