firs_sequences = set([int(x) for x in input().split(" ")])
second_sequences = set([int(x) for x in input().split(" ")])
for _ in range(int(input())):
    first_command, *data = input().split()
    command = first_command + " " + data.pop(0)
    if command == "Add First":
        [firs_sequences.add(int(j)) for j in data]
    elif command == "Add Second":
        [second_sequences.add(int(i)) for i in data]
    elif command == "Remove First":
        [firs_sequences.discard(int(i)) for i in data]
    elif command == "Remove Second":
        [second_sequences.discard(int(i)) for i in data]
    elif command == "Check Subset":
        if firs_sequences.issubset(second_sequences) or second_sequences.issubset(firs_sequences):
            print("True")
        else:
            print("False")
print(*(sorted(firs_sequences)), sep=", ")
print(*(sorted(second_sequences)), sep=", ")