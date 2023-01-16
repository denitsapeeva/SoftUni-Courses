n, m = [int(x) for x in input().split(" ")]
my_set_n = set()
my_set_m = set()
for i in range(n):
    my_set_n.add(int(input()))
for i in range(m):
    my_set_m.add(int(input()))
my_set = set()

if n >= m:
    my_set = my_set_n.intersection(my_set_m)
else:
    my_set = my_set_m.intersection(my_set_n)
for n in my_set:
    print(n)

