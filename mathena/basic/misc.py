import math
from typing import *


def cuberoot(x: int) -> Union[int, float]:
    if x < 0:
        x = abs(x)
        cube_root = x**(1/3)*(-1)
    else:
        cube_root = x**(1/3)
    return cube_root


def is_perfect_square(num: int) -> bool:
    # If ceil and floor are equal
    # the number is a perfect
    # square
    if math.ceil(math.sqrt(num)) == math.floor(math.sqrt(num)):
        return True
    else:
        return False


def is_perfect_cube(num: int) :
    cube_root = round(num**(1/3))
    # If cube of cube_root is equals to num,
    if cube_root * cube_root * cube_root == num:
        return True
    else:
        return False

