from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    def __init__(self,budget:int):
        self.budget = budget

    @property
    @abstractmethod
    def sponsors(self):
        ...

    @property
    @abstractmethod
    def expenses_per_race(self):
        ...

    def calculate_revenue_after_race(self,race_pos:int):
        revenue = 0
        for position in self.sponsors.values():
            for pos in position:
                if race_pos<=pos:
                    revenue += position[pos]
                    break
        revenue -= self.expenses_per_race
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value