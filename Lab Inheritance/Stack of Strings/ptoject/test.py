from ptoject.stack import Stack

my_stack = Stack()
print(my_stack)
my_stack.push("carrot")
print(my_stack)
my_stack.push("apple")
print(my_stack)
my_stack.pop()
print(my_stack.is_empty())
print(my_stack)
for i in range(len(my_stack.data)):
    my_stack.pop()
print(my_stack.is_empty())