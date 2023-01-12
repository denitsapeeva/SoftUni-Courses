my_string = input().split(" ")
reversed_string = []
while my_string:
    take = my_string.pop()
    reversed_string.append(take)
print(' '.join(reversed_string))
