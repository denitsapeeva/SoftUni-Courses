n = int(input())
my_set = set()
for _ in range(n):
    my_input = input().split()
    for value in my_input:
        my_set.add(value)
for value in my_set:
    print(value)
