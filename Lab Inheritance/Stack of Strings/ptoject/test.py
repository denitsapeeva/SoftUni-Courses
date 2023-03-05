from ptoject.stack import Stack

my_stack = Stack()
print(my_stack.__str__())
my_stack.push("carrot")
print(my_stack.__str__())
my_stack.push("apple")
print(my_stack.__str__())
my_stack.pop()
print(my_stack.is_empty())
print(my_stack.__str__())
for i in range(len(my_stack.data)):
    my_stack.pop()
print(my_stack.is_empty())