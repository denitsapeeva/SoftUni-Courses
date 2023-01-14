all_cars_list = [input() for _ in range(int(input()))]
all_cars_numbers = set()
for all in all_cars_list:
    direction,car_number = all.split(", ")
    if direction == "IN":
        all_cars_numbers.add(car_number)
    elif direction == "OUT":
        all_cars_numbers.remove(car_number)
if all_cars_numbers:
    for car in all_cars_numbers:
        print(car)
else:
    print("Parking Lot is Empty")

