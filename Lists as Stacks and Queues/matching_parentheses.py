my_expression = input()
start_index = []
for i in range(len(my_expression)):

    if my_expression[i] == '(':
        start_index.append(i)
    elif my_expression[i] == ')':
        now = start_index.pop()
        print(my_expression[now:i+1])
