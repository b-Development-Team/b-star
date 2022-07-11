from random import choice
from traceback import format_exc

from typing import List, Union

import discord
from func_timeout import func_timeout, FunctionTimedOut
from lark import Tree

from src.interpreter.Codebase import Codebase
from src.interpreter.error_messages import unfunny_errmsg
from src.interpreter.expression import Expression

# the discord user property is used for global ownership checking
import src.interpreter.globals as globals
from src.interpreter.parse import parseCode
from src.interpreter.tempFunctionsFile import functions


def runCode(code: Tree, user: Union[discord.User, None] = None, arguments: List[str] = None):
    try:
        return func_timeout(30, runCodeSandbox, args=(code, user, arguments))
    except FunctionTimedOut:
        return returnError("RUNTIME", "Timed out! (More than 30 seconds)")
    except Exception as error:
        return error


def runCodeSandbox(code: Tree, user: Union[discord.User, None] = None, arguments: List[str] = None):
    # TODO: Trim up to three backticks from beginning and end of code
    parsed_code = parseCode(code).children
    globals.codebase = Codebase(parsed_code, user, arguments)
    globals.codebase.functions = globals.codebase.functions | functions

    for i, statement in enumerate(parsed_code):
        try:
            readLine(statement)
        except Exception as error:
            return returnError(statement, error, i)

    # print(codebase.variables)
    # print(codebase.output)
    if len(globals.codebase.pmoutput) < 2001 and len(globals.codebase.pmoutput) != 0 and not globals.codebase.pmoutput.isspace() and globals.codebase.pmmade:
        globals.codebase.giveToBot['pm'] = globals.codebase.pmoutput
    else:
        globals.codebase.output += f"\n\n⚠️: The code has ran successfully, but a PM failed to send due to it being empty or too long! ({len(globals.codebase.pmoutput)} chars)"
    if len(globals.codebase.output) == 0 or globals.codebase.output.isspace():
        return "⚠️: The code has ran successfully, but returned nothing!"
    if len(globals.codebase.output) > 2000:
        return f"⚠️: Output too long, only showing the first 1000 characters:\n\n```{globals.codebase.output[:1000]}```"
    
    globals.codebase.giveToBot['main'] = globals.codebase.output
    print(globals.codebase.giveToBot)
    return globals.codebase.giveToBot


def readLine(statement):
    if type(statement) == str:
        result = statement
    else:
        result = Expression(statement, globals.codebase)

    # this prints the result code if you need it
    # print(result)
    if result is not None:
        globals.codebase.output += str(result)


def returnError(statement, error, i):
    section = statement.pretty()

    errmsg = f"{choice(unfunny_errmsg)}\n\nError of type {type(error).__name__} at ```scala" \
             f"\n{section}" \
             f"```\n**{error}** (Error occurred at line {i + 1})"
    if globals.debug.print_error:
        print(f"{errmsg}\n\n{format_exc()}")  # print stack trace too
    return errmsg
