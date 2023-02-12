def shopping_cart(*args):
    adding_condition = False
    limit = {
        'Soup': 3,
        'Pizza': 4,
        'Dessert': 2
    }
    products_list = {
        'Soup': set(),
        'Pizza': set(),
        'Dessert': set()
    }
    for products in args:
        if products == "Stop":
            break
        else:
            meal = products[0]
            product = products[1]
            if meal in products_list:
                if len(products_list[meal]) < limit[meal]:
                    adding_condition = True
                    products_list[meal].add(product)
    if adding_condition:
        output = ''
        sorted_data = sorted(products_list, key=lambda k: (-len(products_list[k]), k))
        for key in sorted_data:
            output += f'{key}:\n'
            for element in sorted(products_list[key]):
                output += f' - {element}\n'

        return output

    return 'No products in the cart!'


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
