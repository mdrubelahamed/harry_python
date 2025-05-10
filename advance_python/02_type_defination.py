# import typing
from typing import Union, List, Tuple, Dict

# print(dir(typing))


def sum_of_integers(a: int, b: int) -> int:
    return a + b


# print(sum_of_integers(1, 2))


# union in type defination
def remainder(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a % b


print(remainder(11, 2))  # Returns 1 (int)
print(remainder(11.0, 2))  # Returns 1.0 (float)
print(remainder(11, 2.0))  # Returns 1.0 (float)
print(remainder(11.5, 2))  # Returns 1.5 (float)
