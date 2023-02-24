def shop_from_grocery_list(*args):
    budget = args[0]
    grocery_list = args[1]
    products = []
    for n in range(2,len(args)):
        products.append(args[n])
    purchased_products = []
    total_spent = 0

    for product,value in products:
        if product in grocery_list and product not in purchased_products:
            price = value
            if price > budget - total_spent:
                break
            total_spent += price
            purchased_products.append(product)

    if len(purchased_products) == len(grocery_list):
        budget_left = budget - total_spent
        return f"Shopping is successful. Remaining budget: {budget_left:.2f}."
    else:
        missing_products = set(grocery_list) - set(purchased_products)
        return f"You did not buy all the products. Missing products: {', '.join(missing_products)}."
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))