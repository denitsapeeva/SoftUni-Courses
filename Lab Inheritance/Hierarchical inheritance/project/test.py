from project.cat import Cat
from project.dog import Dog

dog = Dog()
cat = Cat()
print(cat.meow() + cat.eat())
print(dog.eat() + dog.bark())