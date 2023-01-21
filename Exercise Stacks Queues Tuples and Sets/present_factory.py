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
    current_material = materials.pop()
    current_magic_level = magic_level.popleft()
    total_magic = current_magic_level * current_material
    if current_material == 0:
        magic_level.appendleft(current_magic_level)
        continue
    elif current_magic_level == 0:
        materials.append(current_material)
        continue
    elif current_material == 0 and current_magic_level == 0:
        continue
    if total_magic in all_presents:
        my_presents.append(all_presents[total_magic])
    elif total_magic >= 0:
        materials.append(current_material + 15)
    elif total_magic < 0:
        materials.append(current_material + current_magic_level)
if "Doll" and "Wooden train" in my_presents or "Teddy bear" and "Bicycle" in my_presents:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials][::-1])}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

[print(f"{toy}: {my_presents.count(toy)}") for toy in sorted(set(my_presents))]
