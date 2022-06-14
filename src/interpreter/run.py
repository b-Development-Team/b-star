from src.interpreter.parser import parse


def run_code(code):
    tree = parse(code)
    output = ""

    # debug
    print(tree)
    print(tree.pretty())

    # we are looking out for: plaintext, functions
    # for now we will call this a block -- we don't know what it is yet
    for block in tree.children:
        match block.data:
            case "function":
                run_function(block)
            case _:  # most likely plaintext
                output += block.children[0]

    return output


def run_function(tree):
    # we now know that the block is a function
    # we need to get the name and arguments
    name = tree.children[0]
    arguments = tree.children[1]

    func = get_function(name)
    if func is None:
        # tell end user that function does not exist
        print("TODO not found")
    else:
        # run the function
        # TODO: add recursive-ness
        # e.g. func.run(arguments)
        print("TODO run function")


# TODO: (this was function_deco.pys job)
def get_function(name):
    return "TODO get function"


# debug, delete once everything is all done
if __name__ == "__main__":
    result = run_code('''
    [DEFINE e 100]
    [VAR e 100]
    ''')
    print(result)
