from collections import deque

food = deque(x for x in input().split(", "))
stamina = deque(x for x in input().split(", "))

climed_peaks = []

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
        elif len(food) == 0 and len(stamina) == 0 and len(climed_peaks) == 0:
            print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")



