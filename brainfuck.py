import re

_size = 30000
_mem = [0] * _size
_memptr = 0
_prog = []
_progptr = 0


#########################
# BrainFuck Interpreter #
#########################
# > : _memptr++
# < : _memptr--
# + : _mem[_memptr]++
# - : _mem[_memptr]--
# . : print(_mem[_memptr])
# , : _mem[_memptr] = input()
# [ : if _mem[_memptr] != 0, Execute block
# ] : if _mem[_memptr] != 0, return to last ]

def _next():
    global _mem, _memptr, _size
    if (_memptr >= _size - 1):
        _memptr = -1
    _memptr += 1

def _prev():
    global _mem, _memptr, _size
    if (_memptr is 0):
        _memptr = _size
    _memptr -= 1

def _add():
    global _mem, _memptr, _size
    _mem[_memptr] += 1

def _sub():
    global _mem, _memptr, _size
    _mem[_memptr] -= 1

def _while(codeArray):
    global _mem, _memptr, _size
    while(True):
        if (_mem[_memptr] == 0):
            break
        interpretBrainFuck(codeArray)

def _input():
    global _mem, _memptr, _size
    _mem[_memptr] = ord()

def _print():
    global _mem, _memptr, _size
    print(chr(_mem[_memptr]), end='')

_operators = {
    '>':_next,
    '<':_prev,
    '+':_add,
    '-':_sub,
    '.':_print,
    ',':_input
}

def tokenize(string):
    global _operators

    out = []
    strIter = iter(string)
    for char in strIter:
        if char is '[':
            out.append(tokenize(strIter))
        elif char is ']':
            break
        elif (_operators.get(char) is not None):
            out.append(char)
        # else it's not a valid character/operator
        # and we send it to the solar system as entropy
    return out

def interpretBrainFuck(tokens):
    for token in tokens:
        if isinstance(token, list):
            _while(token)
        else:
            _operators[token]()

def interpreter(string):
    interpretBrainFuck(tokenize(string))

interpreter("""
    ++++++++
    [
        >++++
        [
            >++
            >+++
            >+++
            >+
            <<<<-
        ]
        >+>+>->>+
        [<]
        <-
    ]
    >>.
    >---.
    +++++++..
    +++.
    >>.
    <-.
    <.
    +++.
    ------.
    --------.
    >>+.
    >++.
""")