from src.interpreter.function_deco import setupFunctions

from src.interpreter.run import runCode


# stolen from https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
# muhahahahahahaha 😈
class Colours:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Stats:
    num = 0
    correctTests = 0
    failedTests = 0


def test(name, code, assumption):
    result = runCode(code)
    correct = result == assumption
    if correct:
        print(Colours.OKGREEN + Colours.BOLD + "✔", name, Colours.ENDC)
        Stats.correctTests += 1
    else:
        print(Colours.FAIL + Colours.BOLD + "✘", name, end="")
        print(f" (Wanted '{assumption}', Got '{result}')")
        Stats.failedTests += 1
    Stats.num += 1


def testAll():
    test("Hello, World!", "Hello, World!", "Hello, World!")
    test("Simple Define", "[DEFINE x 10][VAR x]", "10")
    test("Define with dynamic name", """
        [DEFINE rnd [RANDINT 1 10]]
        [DEFINE [VAR rnd] 10][VAR [VAR rnd]]
    """, "10")
    test("Basic Math", """
        [ADD 1 [SUB 2 [MUL 3 [DIV 4 4]]]]
    """, "0")
    test("Basic Legacy Math", """
        [MATH 1 + [MATH 2 - [MATH 3 * [MATH 4 / 4]]]]
    """, "0")
    test("Basic Comparison", """
        [COMPARE 2 > 3]
    """, "False")
    test("Basic Logic", """
        [IF [COMPARE 2 < 3] "yes" "no"]
    """, "yes")
    test("Basic Functions", """
        [FUNC SQUARE [ARGS "x"]
            [MUL [VAR x] [VAR x]]
        ]
        [SQUARE 5]
    """, "25")

    test("J", "[J 5]", "jjjjj")


if __name__ == "__main__":
    setupFunctions()
    print(Colours.WARNING + "Starting test..." + Colours.ENDC)
    testAll()

    print()
    if Stats.failedTests == 0:
        print(Colours.OKGREEN + Colours.BOLD + f"All {Stats.num} tests passed!" + Colours.ENDC)
    elif Stats.failedTests < Stats.correctTests:
        print(Colours.WARNING + Colours.BOLD + f"{Stats.correctTests} / {Stats.num} passed..." + Colours.ENDC)
    else:
        print(Colours.FAIL + Colours.BOLD + f"{Stats.correctTests} / {Stats.num} passed..." + Colours.ENDC)
