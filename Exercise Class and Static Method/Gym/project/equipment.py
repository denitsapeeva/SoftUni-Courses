class Equipment:
    equipment_id = 1

    def __init__(self, name):
        self.name = name
        self.id = self.get_next_id()
        Equipment.equipment_id += 1

    @staticmethod
    def get_next_id():
        return Equipment.equipment_id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

