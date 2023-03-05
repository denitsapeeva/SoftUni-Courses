from project.food import Food


class Fruit(Food):
    def __init__(self, name, expiration_date):
        Food.expiration_date = expiration_date
        self. name = name