class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')
        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')
        self.sleepy = False


import unittest

class CatTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cat = Cat('Marry')

    def test_size_increased_fed_after_eating(self):
        cat = Cat('Mary')
        cat.eat()
        self.assertEqual(cat.size,1)
        self.assertTrue(cat.fed)

    def test_eat_after_fed(self):
        self.cat.eat()
        with self.assertRaises(Exception) as context:
            self.cat.eat()
        self.assertEqual(str(context.exception), 'Already fed.')

    def test_cannot_sleep_if_not_fed(self):
        cat = Cat('Any')
        with self.assertRaises(Exception) as context:
            cat.sleep()
        self.assertEqual(str(context.exception), 'Cannot sleep while hungry')

    def test_cannot_sleep_after_sleeping(self):
        cat = Cat('Mary')
        cat.eat()
        cat.sleep()
        self.assertFalse(cat.sleepy)


if __name__ == '__main__':
    unittest.main()