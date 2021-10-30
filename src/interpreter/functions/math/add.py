from typing import List

from src.interpreter.expression import Expression


def add(block: List, codebase):
    if type(block[1]) == List and block[1][0] == "ARRAY":
        block = block[1]
    
    result = Expression(block[1], codebase)

    for num in block[2:]:
        result += Expression(num, codebase)
    return result
