from project.animal import Animal
from project.cheetah import Cheetah
from project.lion import Lion
from project.tiger import Tiger
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list[Animal] = []
        self.workers: list[Worker] = []

    def add_animal(self, animal: Animal, price):
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        if self.__budget - price < 0:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"
        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        salary = sum(w.salary for w in self.workers)
        if self.__budget >= salary:
            self.__budget -= salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        tend = sum(a.money_for_care for a in self.animals)
        if self.__budget >= tend:
            self.__budget -= tend
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions: list[Lion] = []
        tigers: list[Tiger] = []
        cheetah: list[Cheetah] = []
        for a in self.animals:
            if a.__class__.__name__ == "Lion":
                lions.append(a)
            elif a.__class__.__name__ == "Cheetah":
                cheetah.append(a)
            elif a.__class__.__name__ == "Tiger":
                tigers.append(a)

        result = [
            f"You have {len(self.animals)} animals",
            f"----- {len(lions)} Lions:",
        ]
        result.extend(lions)

        result.append(f"----- {len(tigers)} Tigers:")
        result.extend(tigers)

        result.append(f"----- {len(cheetah)} Cheetahs:")
        result.extend(cheetah)
        return "\n".join(str(x) for x in result)

    def workers_status(self):
        info = {"Keeper": [], "Caretaker": [], "Vet": []}
        [info[w.__class__.__name__].append(str(w)) for w in self.workers]

        result = [
            f"You have {len(self.workers)} workers",
            f"----- {len(info['Keeper'])} Keepers:",
            *info['Keeper'],
            f"----- {len(info['Caretaker'])} Caretakers:",
            *info['Caretaker'],
            f"----- {len(info['Vet'])} Vets:",
            *info['Vet'],
        ]

        return "\n".join(result)
