from project.band_members.musician import Musician


class Drummer(Musician):

    @staticmethod
    def available_skills():
        return ["play the drums with drumsticks",
                "play the drums with drum brushes",
                "read sheet music"]
