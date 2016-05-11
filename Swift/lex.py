#------------------------------------------------------------
# lex.py
#
# Swift tokenizer
# ------------------------------------------------------------

import ply.lex as lex

reserved = {
	'BOOL'	: 'bool',
    'TRUE'	: 'true',
    'FALSE'	: 'false',
    'IF'	: 'if',
    'ELSE'	: 'else',
    'VAR'   : 'var',
    'LET'   : 'let',
    'INT'	: 'int',
    'STRING': 'string',
    'PRINT' : 'print'
}


tokens = [
          'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LCURLY', 'RCURLY',\
          'AND_OP', 'OR_OP', 'EQ_OP', 'NE_OP', 'LE_OP', 'GE_OP', 'LT_OP', 'GT_OP', \
          'PLUS', 'MINUS', 'MULT', 'DIV', \
          'INTEGER', 'VALSTRING', 'SQUOTE', 'IDENTIFIER', 'EQUALS', \
          'BOOL', 'TRUE', 'FALSE', 'IF', 'ELSE', 'VAR', 'LET', 'INT', 'STRING', 'PRINT'			
         ]

literals = ['.', ]

t_AND_OP = r'&&'
t_OR_OP = r'\|\|'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\['
t_RBRACE = r'\]'
t_LCURLY = r'{'
t_RCURLY = r'}'
t_EQ_OP = r'=='
t_NE_OP = r'!='
t_LE_OP = r'<='
t_GE_OP = r'>='
t_LT_OP = r'<'
t_GT_OP = r'>'
t_EQUALS = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_SQUOTE = r'\''

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reserved:
        t.type = t.value.upper()
    return t

def t_VALSTRING(t):
    r'"[a-zA-Z0-9_+\*\- :,.!]*"'
    t.type = "STRING" 
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

lex.lex()

if __name__ == '__main__':
    lex.runmain()
