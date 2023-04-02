from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TestTruckDriver(TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver('ivan', 10)

    def test_init(self):
        self.assertEqual(self.driver.name, "ivan")
        self.assertEqual(self.driver.money_per_mile, 10)
        self.assertEqual(self.driver.available_cargos, {})
        self.assertEqual(self.driver.earned_money, 0)
        self.assertEqual(self.driver.miles, 0)

    def test_earned_money(self):
        self.driver.earned_money += 100
        self.assertEqual(self.driver.earned_money, 100)

    def test_earned_money_ex(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money -= 100
        self.assertEqual("ivan went bankrupt.", str(ve.exception))

    def test_add_cargo_if_already_added(self):
        self.driver.available_cargos["Burgas"] = 30
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Burgas", 25)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_ok(self):
        result = self.driver.add_cargo_offer("Burgas", 25)
        self.assertEqual(self.driver.available_cargos["Burgas"], 25)
        self.assertEqual(result, "Cargo for 25 to Burgas was added as an offer.")

    def test_drive_best_cargo_exception(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)

    def test_drive_best_cargo_offer(self):
        self.driver.add_cargo_offer("Burgas", 25)
        self.driver.add_cargo_offer("Sofia",330)
        self.driver.add_cargo_offer("Pomorie",25)
        self.assertEqual(0,self.driver.earned_money)
        self.assertEqual(0,self.driver.miles)
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(3280, self.driver.earned_money)
        self.assertEqual(330, self.driver.miles)
        self.assertEqual(result, f"ivan is driving 330 to Sofia.")

    def test_eat(self):
        self.driver.add_cargo_offer("Burgas", 250)
        self.driver.drive_best_cargo_offer()
        self.assertEqual(self.driver.earned_money, 2480)

    def test_sleep(self):
        self.driver.add_cargo_offer("Burgas", 1000)
        self.driver.drive_best_cargo_offer()
        self.assertEqual(self.driver.earned_money, 9875)

    def test_pump_gas(self):
        self.driver.add_cargo_offer("Burgas", 1500)
        self.driver.drive_best_cargo_offer()
        self.assertEqual(self.driver.earned_money, 14335)

    def test_repair_truck(self):
        self.driver.add_cargo_offer("Burgas", 10000)
        self.driver.drive_best_cargo_offer()
        self.assertEqual(self.driver.earned_money, 88250)

    def test_repr(self):
        result = self.driver.__repr__()
        self.assertEqual(result,"ivan has 0 miles behind his back.")


if __name__ == '__main__':
    main()
