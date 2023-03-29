from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero('hero', 1, 100, 60)
        self.enemy = Hero('enemy', 1, 50, 100)

    def test_init(self):
        self.assertEqual(self.hero.username, 'hero')
        self.assertEqual(self.hero.level, 1)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 60)

    def test_battle_cannot_fight_yourself(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself",str(ex.exception))

    def test_lower_health(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as vl:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest",str(vl.exception))

    def test_lower_enemy_health(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as vl:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight enemy. He needs to rest",str(vl.exception))

    def test_real_battle(self):
        result = self.hero.battle(self.enemy)
        self.assertEqual(self.hero.health,0)
        self.assertEqual(self.enemy.health,-10)
        self.assertEqual(result,"Draw")


    def test_win_case(self):
        self.enemy.damage = 90
        result = self.hero.battle(self.enemy)
        self.assertEqual(self.hero.level,2)
        self.assertEqual(self.hero.health,15)
        self.assertEqual(self.hero.damage,65)
        self.assertEqual(result,"You win")

    def test_lose_case(self):
        self.enemy.health = 100
        result =self.hero.battle(self.enemy)
        self.assertEqual(self.enemy.level,2)
        self.assertEqual(self.enemy.health,45)
        self.assertEqual(self.enemy.damage,105)
        self.assertEqual(result,"You lose")

    def test_str_method(self):
        self.assertEqual("Hero hero: 1 lvl\n"+
               "Health: 100\n" +
               "Damage: 60\n",str(self.hero))

    if __name__ == '__main__':
        main()
