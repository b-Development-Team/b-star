from src.interpreter.userfunction import UserFunction


def func(name, args, code):
    # name = Expression(block[1], codebase)

    # Assume block[2] is an array (it better be)
    args = dict(enumerate(args))

    UserFunction(name, args, code, True, codebase)
