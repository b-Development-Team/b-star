import Config.b_star_interpreter.globals as globals
from Config.b_star_interpreter.exceptions import BStarUndefinedVariableException


def var(item, index):
    for val in reversed(globals.codebase.variables):
        if item in val:
            return val[item] if index == "" else val[item][index]
    raise BStarUndefinedVariableException(f"variable not found: {item}")
