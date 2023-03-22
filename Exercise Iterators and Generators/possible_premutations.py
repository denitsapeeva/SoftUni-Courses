from itertools import permutations
from typing import List


def possible_permutations(numbers:List):
    for el in list(permutations(numbers)):
        yield list(el)


[print(n) for n in possible_permutations([1, 2, 3])]