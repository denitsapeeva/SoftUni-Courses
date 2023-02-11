from collections import deque

food = deque(int(x) for x in input().split(", "))
stamina = deque(int(x) for x in input().split(", "))

climed_peaks = []
stop_the_program = False

all_peaks = {"Vihren": 80,
             "Kutelo": 90,
             "Banski Suhodol": 100,
             "Polezhan": 60,
             "Kamenitza": 70
             }

for key,value in all_peaks.items():
    while True:
        my_sum = food.pop() + stamina.popleft()
        if my_sum >= value:
            climed_peaks.append(key)
            break
        if len(food) == 0 and len(stamina) == 0 and len(climed_peaks) < 5:
            print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
            stop_the_program = True
            break
    if stop_the_program:
        break
if len(climed_peaks) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
if climed_peaks:
    print("Conquered peaks:\n" + '\n'.join(climed_peaks))





