from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms: list[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        my_room = next(filter(lambda r: r.number == room_number, self.rooms))
        result = my_room.take_room(people)
        if result:
            return result

        self.guests += people

    def free_room(self, room_number):
        my_room = next(filter(lambda r: r.number == room_number, self.rooms))
        guests = my_room.guests
        result = my_room.free_room()
        if result:
            return result

        self.guests -= guests

    def status(self):
        free_rooms = [r.number for r in self.rooms if r.is_taken == False]
        taken_rooms = [r.number for r in self.rooms if r.is_taken]
        return f"Hotel {self.name} has {self.guests} total guests\nFree rooms: {', '.join(str(x) for x in free_rooms)}\nTaken rooms: {', '.join(str(x) for x in taken_rooms)}"
