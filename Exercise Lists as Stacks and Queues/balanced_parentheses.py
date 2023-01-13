my_expression = input()
right_expression = []
left_expression = []
stop_index = 0
my_bool = True
for i in range(len(my_expression)):
    if my_expression[i] != ')':
        right_expression.append(my_expression[i])
    else:
        stop_index = i
        break
for j in range(stop_index,len(my_expression)):
    left_expression.append(my_expression[j])

if len(right_expression) == len(left_expression):
    while right_expression:
        right = right_expression.pop()
        left = left_expression.pop(0)
        if right == '{' and left == '}':
            continue
        elif right == '(' and left == ')':
            continue
        elif right == '[' and left == ']':
            continue
        else:
            my_bool = False
else:
    my_bool = False

if my_bool:
    print("YES")
else:
    print("NO")


