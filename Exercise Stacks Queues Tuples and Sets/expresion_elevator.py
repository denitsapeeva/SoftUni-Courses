from collections import deque
from functools import reduce

my_expression = input().split()
idx = 0
my_reduce = {
    "*": lambda i: reduce(lambda a, b: int(a) * int(b), my_expression[:i]),
    "+": lambda i: reduce(lambda a, b: int(a) + int(b), my_expression[:i]),
    "-": lambda i: reduce(lambda a, b: int(a) - int(b), my_expression[:i]),
    "/": lambda i: reduce(lambda a, b: int(a) / int(b), my_expression[:i]),

}
while idx < len(my_expression):
    element = my_expression[idx]
    if element in "*-/+":
        result = my_reduce[element](idx)
        my_expression = my_expression[idx:]
        my_expression[0] = result
        idx = 0
    idx += 1
print(int(my_expression[0]))
