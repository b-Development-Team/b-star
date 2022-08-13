import src.interpreter.globals as globals


def args(index):
    if index == "":
        return globals.codebase.arguments
    try:
        return globals.codebase.arguments[index]
    except IndexError:
        return ""
