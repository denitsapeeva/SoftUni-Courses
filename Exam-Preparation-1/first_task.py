from collections import deque

textiles = deque(int(x) for x in input().split())
medicament = deque(int(x) for x in input().split())
create = False

items = {
    "Patch": 30,
    "Bandage": 40,
    "MedKit": 100
}

created_items = {

}

while textiles and medicament:
    t = textiles.popleft()
    m = medicament.pop()
    my_sum = t + m
    remaining_resources = 0
    for k, v in items.items():
        if v == my_sum:
            if k in created_items:
                created_items[k] += 1
            else:
                created_items[k] = 1
            create = True
    if my_sum > items["MedKit"]:
        if "MedKit" in created_items:
            created_items["MedKit"] += 1
        else:
            created_items["MedKit"] = 1
        medicament[-1] += my_sum - 100
        create = True
    if not create:
        medicament.append(m + 10)
    create = False

if not textiles and not medicament:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicament:
    print("Medicaments are empty.")

if created_items:
    created_data = sorted(created_items.items(), key=lambda x: (-x[1], x[0]))
    for items in created_data:
        print(f"{items[0]} - {items[1]}")

if medicament:
    new_medical = []
    while medicament:
        new_medical.append(medicament.pop())
    print(f"Medicaments left: {', '.join(str(x) for x in new_medical)}")
if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")
