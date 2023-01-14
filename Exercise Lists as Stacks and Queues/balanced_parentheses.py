from _collections import deque
parentheses = deque(input())
open_paranthesis = deque()
while parentheses:
    left_parantheses = parentheses.popleft()
    if left_parantheses in "({[":
        open_paranthesis.append(left_parantheses)
    elif not open_paranthesis:
        print("NO")
        break
    else:
        if f"{open_paranthesis.pop() + left_parantheses}" not in "{}[]()":
            print("NO")
            break
else:
    print("YES")


