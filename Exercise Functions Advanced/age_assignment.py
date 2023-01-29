def age_assignment(*args,**kwargs):
    all_names = []
    for name in args:
        for key,value in kwargs.items():
            if name.startswith(key):
                all_names.append(f"{name} is {value} years old.")

    return "\n".join(sorted(all_names))




print(age_assignment("Peter", "George", G=26, P=19))
