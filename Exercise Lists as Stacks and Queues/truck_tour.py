from _collections import deque

nums_of_pumps = int(input())
pumps_data = deque()
for _ in range(nums_of_pumps):
    pumps_data1 = [int(x) for x in input().split()]
    pumps_data.append(pumps_data1)
pumps_data_copy = pumps_data.copy()
index = 0
gas_in_tank = 0
while pumps_data_copy:
    petrol, distance = pumps_data_copy.popleft()
    gas_in_tank += petrol
    if gas_in_tank - distance < 0:
        pumps_data.rotate(-1)
        pumps_data_copy = pumps_data.copy()
        index += 1
        gas_in_tank = 0
    else:
        gas_in_tank -= distance
print(index)
