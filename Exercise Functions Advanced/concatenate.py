def concatenate(*args, **kwargs):
    my_string = ""
    for n in args:
        my_string += n

    for key, value in kwargs.items():
        if key in my_string:
            my_string = my_string.replace(key, value)
    return my_string


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
