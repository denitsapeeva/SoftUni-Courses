from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.car = Vehicle(300, 100)

    def test_init(self):
        self.assertEqual(self.car.fuel, 300)
        self.assertEqual(self.car.capacity, 300)
        self.assertEqual(self.car.horse_power, 100)
        self.assertEqual(self.car.fuel_consumption, 1.25)

    def test_drive(self):
        self.car.drive(60)
        self.assertEqual(self.car.fuel, 225)

    def test_drive_with_not_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(300)
        self.assertEqual("Not enough fuel",str(ex.exception))

    def test_refuel(self):
        self.car.fuel = 50
        self.car.refuel(100)
        self.assertEqual(self.car.fuel,150)

    def test_too_much_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(50)
        self.assertEqual("Too much fuel",str(ex.exception))

    def test_str_method(self):
        self.assertEqual(self.car.__str__(),"The vehicle has 100 horse power with 300 fuel left and 1.25 fuel consumption")

    if __name__ == '__main__':
        main()
