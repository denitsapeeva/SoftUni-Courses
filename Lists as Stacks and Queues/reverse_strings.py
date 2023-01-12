stack = list(input())
new_stack = []
while stack:
    pops = stack.pop()
    new_stack.append(pops)

print("".join(new_stack))