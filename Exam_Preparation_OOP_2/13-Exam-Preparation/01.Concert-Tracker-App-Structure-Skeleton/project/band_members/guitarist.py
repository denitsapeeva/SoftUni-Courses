from project.band_members.musician import Musician


class Guitarist(Musician):

    @staticmethod
    def available_skills():
        return ["play metal",
                "play rock",
                "play jazz"]
