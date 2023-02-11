size_of_matrix = int(input())
car_number = input()
car_coordinate = [0, 0]
race = []
tunnel_coordinate = []
kilometers = 0
finished = False


for i in range(size_of_matrix):
    race.append(input().split(" "))
    if "T" in race[i]:
        tunnel_coordinate.append([i, race[i].index("T")])


while True:
    command = input()
    if command == "End":
        break
    if command == "up":
        car_coordinate[0] = car_coordinate[0] - 1
    if command == "down":
        car_coordinate[0] = car_coordinate[0] + 1
    if command == "right":
        car_coordinate[1] = car_coordinate[1] + 1
    if command == "left":
        car_coordinate[1] = car_coordinate[1] - 1
    kilometers += 10

    if race[car_coordinate[0]][car_coordinate[1]] == "T":
        if car_coordinate == tunnel_coordinate[0]:
            car_coordinate = tunnel_coordinate[1]
        elif car_coordinate == tunnel_coordinate[1]:
            car_coordinate = tunnel_coordinate[0]
        race[tunnel_coordinate[0][0]][tunnel_coordinate[0][1]] = '.'
        race[tunnel_coordinate[1][0]][tunnel_coordinate[1][1]] = '.'
        kilometers += 20
    if race[car_coordinate[0]][car_coordinate[1]] == "F":
        race[car_coordinate[0]][car_coordinate[1]] = "C"
        print(f"Racing car {car_number} finished the stage!")
        finished = True
        break
if not finished:
    print(f"Racing car {car_number} DNF.")
    race[car_coordinate[0]][car_coordinate[1]] = "C"
print(f"Distance covered {kilometers} km.")
[print(*row,sep="")for row in race]



