from collections import deque

materials = deque(int(x) for x in input().split())
magic_level = deque(int(x) for x in input().split())
my_presents = []
all_presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}
while materials and magic_level:
    current_material = materials.pop() if magic_level[0] or not materials[0] else 0
    current_magic_level = magic_level.popleft() if current_material or not magic_level[0] else 0
    if not current_magic_level:
        continue
    total_magic = current_magic_level * current_material

    if all_presents.get(total_magic):
        my_presents.append(all_presents[total_magic])
    elif total_magic > 0:
        materials.append(current_material + 15)
    elif total_magic < 0:
        materials.append(current_material + current_magic_level)
if {"Doll","Wooden train"}.issubset(my_presents) or {"Teddy bear","Bicycle"}.issubset(my_presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials][::-1])}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

[print(f"{toy}: {my_presents.count(toy)}") for toy in sorted(set(my_presents))]

