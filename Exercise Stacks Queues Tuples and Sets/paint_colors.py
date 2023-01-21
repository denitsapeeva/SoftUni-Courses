from collections import deque

my_string = deque(input().split())

colors ={"red", "yellow", "blue", "orange", "purple", "green"}
req_colors={
"orange":{"red","yellow"},
"purple":{"red","blue"},
"green": {"yellow","bue"},
}
my_colors = []
while my_string:
    first_el = my_string.popleft()
    second_el = my_string.pop() if my_string else ''
    for color in (first_el+second_el,second_el+first_el):
        if color in colors:
            my_colors.append(color)
            break
    else:
        for el in (first_el[:-1],second_el[:-1]):
            if el:
                my_string.insert(len(my_string)//2,el)
for color in set(req_colors.keys()).intersection(my_colors):
    if not req_colors[color].issubset(my_colors):
        my_colors.remove(color)
print(my_colors)