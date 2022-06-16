from lark import Lark

bstargrammar = r"""
start: arg*

?arg:
    | "true" -> true
    | "false" -> false
    | ESCAPED_STRING
    | SIGNED_NUMBER
    | function
    | array
    | UNESCAPED

string: ESCAPED_STRING

block: UNESCAPED
args: arg*

array: "{" [arg ("," arg)*] "}"

function: ("[") block args ("]")

NONFUNCS: ACTUALLYEVERYTHING*
DIGIT: "0".."9"
LCASE_LETTER: "a".."z"
UCASE_LETTER: "A".."Z"
LETTER: UCASE_LETTER | LCASE_LETTER
ALPHANUMERIC: ("_" | "." | LETTER | DIGIT)+
SUPERALPHANUMERIC: (ALPHANUMERIC | "+" | "*" | "-" | "/" | "^" | "=" | "!")+
EVERYTHING: /.^\s/+
UNESCAPED: (SUPERALPHANUMERIC | EVERYTHING)
ACTUALLYEVERYTHING: /\s\S/+



// imports from common library my beloved
%import common.WORD
%import common.ESCAPED_STRING
%import common.SIGNED_NUMBER

%import common.C_COMMENT
%import common.WS
%ignore WS
%ignore C_COMMENT"""
parser = Lark(bstargrammar)


def parseCode(code):
    return parser.parse(code)
