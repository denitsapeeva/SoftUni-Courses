def even_odd(*args):
    type_of_numbers = args[-1]
    filtered_numbers = []
    for n in args[:-1]:
        if type_of_numbers == "odd":
            if n % 2 != 0:
                filtered_numbers.append(n)
        elif type_of_numbers == "even":
            if n % 2 == 0:
                filtered_numbers.append(n)
    return filtered_numbers


