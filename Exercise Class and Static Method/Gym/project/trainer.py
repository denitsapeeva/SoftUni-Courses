class Trainer:
    trainer_id = 1
    def __init__(self, name):
        self.name = name
        self.id = Trainer.trainer_id
        self.get_next_id()

    @staticmethod
    def get_next_id():
        Trainer.trainer_id += 1

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

