from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income = 0

    def add_delicacy(self, type_delicacy, name, price) -> str:
        valid_names = ["Gingerbread", "Stolen"]
        delicacy = [d for d in self.delicacies if d.name == name]
        if delicacy:
            raise Exception(f"{name} already exists!")
        if type_delicacy not in valid_names:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        if type_delicacy == "Gingerbread":
            self.delicacies.append(Gingerbread(name, price))
        elif type_delicacy == "Stolen":
            self.delicacies.append(Stolen(name, price))

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth, booth_number, capacity):
        valid_booths = ["Open Booth", "Private Booth"]
        booth = [b for b in self.booths if b.booth_number == booth_number]
        if booth:
            raise Exception(f"Booth number {booth_number} already exists!")
        if type_booth not in valid_booths:
            raise Exception(f"{type_booth} is not a valid booth!")
        if type_booth == "Open Booth":
            self.booths.append(OpenBooth(booth_number, capacity))
        elif type_booth == "Private Booth":
            self.booths.append(PrivateBooth(booth_number, capacity))
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        try:
            booth = next(filter(lambda b: b.capacity >= number_of_people and b.is_reserved == False, self.booths))
        except StopIteration:
            raise Exception(f"No available booth for {number_of_people} people!")
        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number, delicacy_name):
        try:
            booth = next(filter(lambda b: b.booth_number== booth_number, self.booths))
        except StopIteration:
            raise Exception(f"Could not find booth {booth_number}!")
        try:
            delicacy = next(filter(lambda d: d.name == delicacy_name,self.delicacies))
        except StopIteration:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number):
        booth = [b for b in self.booths if b.booth_number == booth_number][0]
        bill = booth.price_for_reservation + sum(d.price for d in booth.delicacy_orders)
        self.income += bill
        booth.delicacy_orders.clear()
        booth.is_reserved = False
        booth.price_for_reservation = 0
        return f"Booth {booth_number}:\n" \
               f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
