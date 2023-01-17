number = int(input())
longest_intersection = set()
for _ in range(number):
    first_range, second_range =[x.split(",") for x in input().split("-")]
    first_intersection = set()
    second_intersecton = set()
    for i in range(int(first_range[0]), int(first_range[1])+1):
        first_intersection.add(i)
    for j in range(int(second_range[0]), int(second_range[1])+1):
        second_intersecton.add(j)
    current_intersection = first_intersection.intersection(second_intersecton)
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(f"Longest intersection is [{', '.join(str(x) for x in longest_intersection)}] with length {len(longest_intersection)}")

