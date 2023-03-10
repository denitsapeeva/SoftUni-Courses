from project.beverage.hot_beverage import HotBeverage


class Coffe(HotBeverage):
    MILLITERS = 50
    PRICE = 3.5

    def __init__(self, name, caffeine):
        super().__init__(name, Coffe.PRICE,Coffe.MILLITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine
