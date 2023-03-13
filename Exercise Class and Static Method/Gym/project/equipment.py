class Equipment:
    equipment_id = 1

    def __init__(self, name):
        self.name = name
        self.id = Equipment.equipment_id
        self.get_next_id()

    @staticmethod
    def get_next_id():
        Equipment.equipment_id += 1

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

