from lark import Lark

bstargrammar = r"""
start: bstar*
    
?bstar:
    | function
    | ALLBUTBRACKETS
?arg:
    | "true" -> true
    | "false" -> false
    | string
    | SIGNED_NUMBER -> number
    | function
    | array
    | unescaped_string

string: ESCAPED_STRING

block: ALPHANUMERIC
args: arg*

array: "{" [arg ("," arg)*] "}"

function: ("[") block args ("]")

unescaped_string: ALPHANUMERIC
ALLBUTBRACKETS: ALLEXCEPTBRACKETS+


DIGIT: "0".."9"
LCASE_LETTER: "a".."z"
UCASE_LETTER: "A".."Z"
LETTER: UCASE_LETTER | LCASE_LETTER
ALPHANUMERIC: (ALLNONCONFLICTING)+
ALLNONCONFLICTING: /[^\[\]0-9\{\}\"\s]/
ALLEXCEPTBRACKETS: /[^\[\]]/


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
