n = int(input())
my_stack = []
for i in range(n):
    queries = input().split(" ")
    command = queries[0]
    if command == '1':
        my_stack.append(int(queries[1]))
    elif command == '2' and my_stack:
        my_stack.pop()
    elif command == '3' and my_stack:
        print(max(my_stack))
    elif command == '4' and my_stack:
        print(min(my_stack))
str_stack = []
while my_stack:
    str_stack.append(str(my_stack.pop()))
print(', '.join(str_stack))
