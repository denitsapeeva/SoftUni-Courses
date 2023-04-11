from project.band_members.musician import Musician


class Singer(Musician):

    @staticmethod
    def available_skills():
        return ["sing high pitch notes","sing low pitch notes"]