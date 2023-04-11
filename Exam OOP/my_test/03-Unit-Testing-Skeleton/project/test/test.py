from unittest import TestCase, main

from project.tennis_player import TennisPlayer


class TestTennisPlayer(TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer('Any', 22, 3)

    def test_init(self):
        self.assertEqual(self.player.name, "Any")
        self.assertEqual(self.player.age, 22)
        self.assertEqual(self.player.points, 3)
        self.assertEqual(self.player.wins, [])

    def test_name_error(self):
        with self.assertRaises(ValueError) as ve:
            TennisPlayer("An", 22, 3)
        self.assertEqual(str(ve.exception), "Name should be more than 2 symbols!")

    def test_age_error(self):
        with self.assertRaises(ValueError) as ve:
            TennisPlayer("Andy", 17, 3)
        self.assertEqual(str(ve.exception), "Players must be at least 18 years of age!")

    def test_add_new_win(self):
        self.player.add_new_win("Base")
        self.assertEqual(self.player.wins[0], "Base")
        self.player.add_new_win("Bases")
        self.assertEqual(self.player.wins[1], "Bases")

    def test_add_new_win_already_added(self):
        self.player.add_new_win("Base")
        result = self.player.add_new_win("Base")
        self.assertEqual(result, "Base has been already added to the list of wins!")

    def test_lt(self):
        player_2 = TennisPlayer('Anyby', 22, 5)
        result = self.player.__lt__(player_2)
        self.assertEqual(result, "Anyby is a top seeded player and he/she is better than Any")

    def test_lt_same(self):
        player_2 = TennisPlayer('Anyby', 22, 3)
        result = self.player.__lt__(player_2)
        self.assertEqual(result, "Any is a better player than Anyby")

    def test_lt_other(self):
        player_2 = TennisPlayer('Anyby', 22, 1)
        result = self.player.__lt__(player_2)
        self.assertEqual(result, "Any is a better player than Anyby")

    def test_str(self):
        result = self.player.__str__()
        self.assertEqual(result, "Tennis Player: Any\n"
                                 "Age: 22\n"
                                 "Points: 3.0\n"
                                 "Tournaments won: ")

    def test_str_with_won(self):
        self.player.add_new_win("Base")
        self.player.add_new_win("Base1")
        result = self.player.__str__()
        self.assertEqual(result, "Tennis Player: Any\n"
                                 "Age: 22\n"
                                 "Points: 3.0\n"
                                 "Tournaments won: Base, Base1")


if __name__ == "__main__":
    main()
