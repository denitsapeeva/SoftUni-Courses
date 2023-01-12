quantity_of_food = int(input())
orders = [int(x) for x in input().split(" ")]
print(max(orders))
while orders:
    if orders[0] <= quantity_of_food:
        quantity_of_food -= orders.pop(0)
    else:
        break

if orders:
    str_orders = [str(x) for x in orders]
    print(f"Orders left: {' '.join(str_orders)}")
else:
    print("Orders complete")