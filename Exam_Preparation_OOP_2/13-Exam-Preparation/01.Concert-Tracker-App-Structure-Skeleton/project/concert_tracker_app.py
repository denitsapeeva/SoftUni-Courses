from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {"Guitarist": Guitarist,
                            "Drummer": Drummer,
                            "Singer": Singer
                            }

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN_TYPES.keys():
            raise ValueError("Invalid musician type!")
        musician = [m for m in self.musicians if m.name == name]
        if musician:
            raise Exception(f"{name} is already a musician!")
        self.musicians.append(self.VALID_MUSICIAN_TYPES[musician_type](name, age))
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band = [b for b in self.bands if b.name == name]
        if band:
            raise Exception(f"{name} band is already created!")
        self.bands.append(Band(name))
        return f"{name} was created."

    def create_concert(self, genre, audience, ticket_price, expenses, place):
        concert = [c for c in self.concerts if c.place == place]
        if concert:
            raise Exception(f"{place} is already registered for {genre} concert!")
        self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name, band_name):
        try:
            musician = next(filter(lambda m: m.name == musician_name, self.musicians))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a musician!")

        try:
            band = next(filter(lambda b: b.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")
        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name, band_name):
        try:
            band = next(filter(lambda b: b.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")
        try:
            musician = next(filter(lambda m: m.name == musician_name, band.members))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place, band_name):
        band = [b for b in self.bands if b.name == band_name][0]
        concert = [p for p in self.concerts if p.place == concert_place][0]
        bands_type = {"Guitarist": 0,
                      "Drummer": 0,
                      "Singer": 0
                      }
        bands_skills = {"Guitarist": [],
                        "Drummer": [],
                        "Singer": []
                        }
        for member in band.members:
            bands_type[member.__class__.__name__] += 1
            for skill in member.skills:
                bands_skills[member.__class__.__name__].append(skill)
        if bands_type["Guitarist"] < 1 or bands_type["Drummer"] < 1 or bands_type["Singer"] < 1:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")
        if concert.genre == "Rock":
            drums = False
            sing = False
            guitar = False
            for skill in bands_skills["Guitarist"]:
                if skill == "play rock":
                    guitar = True

            for skill in bands_skills["Singer"]:
                if skill == "sing high pitch notes":
                    sing = True

            for skill in bands_skills["Drummer"]:
                if skill == "play the drums with drumsticks":
                    drums = True
            if not sing and not guitar and not drums:
                raise Exception(f"The {band_name} band is not ready to play at the concert!")
            else:
                profit = (concert.audience*concert.ticket_price)-concert.expenses
                return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."

        if concert.genre == "Metal":
            drums = False
            sing = False
            guitar = False
            for skill in bands_skills["Guitarist"]:
                if skill == "play metal":
                    guitar = True

            for skill in bands_skills["Singer"]:
                if skill == "sing low pitch notes":
                    sing = True

            for skill in bands_skills["Drummer"]:
                if skill == "play the drums with drumsticks":
                    drums = True
            if not sing and not guitar and not drums:
                raise Exception(f"The {band_name} band is not ready to play at the concert!")
            else:
                profit = (concert.audience*concert.ticket_price)-concert.expenses
                return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."

        if concert.genre == "Jazz":
            drums = False
            sing_one = False
            sing_two = False
            guitar = False
            for skill in bands_skills["Guitarist"]:
                if skill == "play jazz":
                    guitar = True

            for skill in bands_skills["Singer"]:
                if skill == "sing low pitch notes":
                    sing_one = True

            for skill in bands_skills["Singer"]:
                if skill == "sing high pitch notes":
                    sing_two = True

            for skill in bands_skills["Drummer"]:
                if skill == "play the drums with drum brushes":
                    drums = True
            if not sing_one and not  sing_two and not guitar and not drums:
                raise Exception(f"The {band_name} band is not ready to play at the concert!")
            else:
                profit = (concert.audience*concert.ticket_price)-concert.expenses
                return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."