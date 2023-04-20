import Config.b_star_interpreter.globals as globals


def args(index: int):
    if index == "":
        return globals.codebase.arguments
    try:
        return globals.codebase.arguments[index]
    except IndexError:
        return ""
