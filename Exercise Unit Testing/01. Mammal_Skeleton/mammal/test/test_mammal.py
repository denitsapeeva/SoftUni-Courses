from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Ari", "monkey", "auau")

    def test_init(self):
        self.assertEqual('Ari', self.mammal.name)
        self.assertEqual("monkey", self.mammal.type)
        self.assertEqual("auau", self.mammal.sound)
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual("Ari makes auau", result)

    def test_get_info(self):
        result = self.mammal.info()
        self.assertEqual("Ari is of type monkey", result)


if __name__ == '__main__':
    main()
