from typing import List

from src.interpreter.expression import Expression


def if_func(block: List, codebase):
    compare = Expression(block[1], codebase)
    true = block[2]
    false = block[3]
    return Expression(true, codebase) if compare else Expression(false, codebase)

