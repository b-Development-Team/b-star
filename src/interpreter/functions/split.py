from typing import List
from src.interpreter.expression import Expression


def split(block: List, codebase):
    string = block[1]
    string = [*string.split(" ")] if len(block) < 3 else [*string.split(block[2])]
    return Expression(["ARRAY", *string], codebase)
