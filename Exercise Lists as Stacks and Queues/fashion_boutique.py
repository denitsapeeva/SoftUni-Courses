all_clothes = [int(x) for x in input().split(" ")]
capacity_of_rack = int(input())
used_racks = 0
while all_clothes:
    c = all_clothes.pop()
    if all_clothes:
        while c + all_clothes[-1] <= capacity_of_rack:
            c += all_clothes.pop()
            if len(all_clothes) <1:
                break
    used_racks += 1
print(used_racks)


