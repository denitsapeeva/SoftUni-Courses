from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    def setUp(self) -> None:
        self.toy = ToyStore()

    def test_init(self):
        for letter in range(ord('A'), ord('G') + 1):
            self.assertEqual(self.toy.toy_shelf[chr(letter)], None)

    def test_add_toy_if_not_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.toy.add_toy("O", "car")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_existing_toy(self):
        self.toy.add_toy("A", "car")
        with self.assertRaises(Exception) as ex:
            self.toy.add_toy("A", "car")
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_if_shelf_is_taken(self):
        self.toy.add_toy("A", "car")
        with self.assertRaises(Exception) as ex:
            self.toy.add_toy("A", "plane")
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_okey(self):
        result = self.toy.add_toy("A", "car")
        self.assertEqual(self.toy.toy_shelf["A"], "car")
        self.assertEqual(result, "Toy:car placed successfully!")

    def test_remove_toy_from_shelf_that_doesnt_exist(self):
        with self.assertRaises(Exception) as ex:
            self.toy.remove_toy("O", "car")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_doesnt_exist(self):
        self.toy.add_toy("A", "cars")
        with self.assertRaises(Exception) as ex:
            self.toy.remove_toy("A", "car")
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_ok(self):
        self.toy.add_toy("A", "cars")
        result = self.toy.remove_toy("A", "cars")
        self.assertEqual(self.toy.toy_shelf["A"], None)
        self.assertEqual(result, "Remove toy:cars successfully!")


if __name__ == '__main__':
    main()
