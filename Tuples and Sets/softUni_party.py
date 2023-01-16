reservations = set([input() for _ in range(int(input()))])
guests_at_the_party = set()
while True:
    command = input()
    if command == "END":
        break
    guests_at_the_party.add(command)
left_reservations = reservations.difference(guests_at_the_party)
print(len(left_reservations))

for guest in sorted(left_reservations):
    print(guest)
