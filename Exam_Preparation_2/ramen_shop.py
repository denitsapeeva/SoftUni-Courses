from collections import deque

bowls_of_ramen = deque(int(x) for x in input().split(", "))
customer = deque(int(x) for x in input().split(", "))

while bowls_of_ramen and customer:
    current_bowl = bowls_of_ramen.pop()
    current_customer = customer.popleft()
    if current_customer == current_bowl:
        continue
    elif current_customer > current_bowl:
        customer.appendleft(current_customer-current_bowl)
    elif current_customer < current_bowl:
        bowls_of_ramen.append(current_bowl-current_customer)
if not customer:
    print("Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls_of_ramen)}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customer)}")

