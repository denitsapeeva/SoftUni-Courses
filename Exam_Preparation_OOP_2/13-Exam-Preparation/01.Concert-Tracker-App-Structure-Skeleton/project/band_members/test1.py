arr = [3.11, 3.0, 7.6, 5.0, 6.8]


int_arr = [int(num) for num in arr if num.is_integer()]

print("Целите числа в масива са:", int_arr)
