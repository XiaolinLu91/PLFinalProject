import ply.yacc as yacc

from lex import tokens

def p_program(p):
    'program : statements'
    p[0] = p[1]

def p_statements(p):
    '''statements : statement
                  | statements statement'''
    if len(p) > 2:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]

def p_statement(p):
    '''statement : expression
                 | variable_Dec
                 | variable_Reduce
                 | if_statement
                 | print'''
    p[0] = [p[1]]

def p_variable_Reduce(p):
    '''variable_Reduce : IDENTIFIER EQUALS expression'''
    p[0] = ["reduce", p[1], p[2], p[3] ] 

def p_variable_Dec(p):
    '''variable_Dec : LET IDENTIFIER EQUALS expression
                    | VAR IDENTIFIER EQUALS expression'''
    p[0] = [ p[1], p[2], p[4] ]

def p_print(p):
    '''print : PRINT LPAREN RPAREN
             | PRINT LPAREN IDENTIFIER RPAREN
             | PRINT LPAREN INTEGER RPAREN
             | PRINT LPAREN STRING RPAREN'''
    if len(p) > 4:
        p[0] = ["print", p[3] ]
    else:
        p[0] = ["print", ""]

def p_if_statement(p):
    '''if_statement : IF cond_statement code_section
                   | IF cond_statement code_section else_statement'''
    if len(p) > 4:
        p[0] = [ p[1], p[2], p[3], p[4] ]
    else:
        p[0] = [ p[1], p[2], p[3] ]

def p_else_statement(p):
    '''else_statement : ELSE code_section
                     | if_statement'''
    if len(p) > 2:
        p[0] = [ p[1], p[2] ]
    else:
        p[0] = [ p[1] ]

def p_code_section(p):
    'code_section : LCURLY statements RCURLY'
    p[0] = p[2]

def p_cond_statement(p):
    '''cond_statement : thing booleanOP thing
                            | TRUE
                            | FALSE'''
    if len(p) > 2:
        p[0] = [ p[1], p[2], p[3] ]
    else:
        p[0] = [ p[1] ]

def p_expression(p):
    '''expression : conjunction
                  | conjunction OR_OP expression'''
    p[0] = p[1]

def p_conjunction(p):
    '''conjunction : equality
                   | AND_OP equality'''
    if len(p) == 4:
        p[0] = [ p[1], p[2], p[3] ]
    else:
        p[0] = p[1]

def p_booleanOP(p):
    '''booleanOP : equalityOP
              | relationOP'''
    p[0] = p[1]

def p_equality(p):
    '''equality : relation
                | relation equalityOP equality'''
    if len(p) == 4:
        p[0] = [ p[1], p[2], p[3] ]
    else :
        p[0] = p[1]

def p_equalityOP(p):
    '''equalityOP : EQ_OP
            | NE_OP'''
    p[0] = p[1]

def p_relation(p):
    '''relation : addition
                | addition relationOP relation'''
    if len(p) == 4:
        p[0] = [ p[1], p[2], p[3] ]
    else :
        p[0] = p[1]

def p_relationOP(p):
    '''relationOP : LT_OP
             | LE_OP
             | GT_OP
             | GE_OP'''
    p[0] = p[1]

def p_addition(p):
    '''addition : term
                | term additionOP addition'''
    if len(p) == 4:
        p[0] = ["arithmetic", p[1], p[2], p[3]] 
    else :
        p[0] = p[1]

def p_additionOP(p):
    '''additionOP : PLUS
             | MINUS'''
    p[0] = p[1]

def p_term(p):
    '''term : factor
            | factor multiOP term'''
    if len(p) == 4:
        p[0] = ["arithmetic", p[1], p[2], p[3]] 
    else :
        p[0] = p[1]

def p_multiOP(p):
    '''multiOP : MULT
             | DIV'''
    p[0] = p[1]

def p_factor(p):
    'factor : primary'
    if len(p) == 4:
        p[0] = [ p[1], p[2], p[3] ]
    else:
        p[0] = p[1]

def p_primary(p):
    '''primary : literal'''
    p[0] = p[1]

def p_literal(p):
    '''literal : INTEGER
               | STRING
               | IDENTIFIER
               | TRUE
               | FALSE'''
    p[0] = p[1]

def p_thing(p):
    '''thing : INTEGER
            | IDENTIFIER
            | STRING'''
    p[0] = p[1]

def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    print "Syntax error!! ", p

# Build the parser
# Use this if you want to build the parser using SLR instead of LALR
# yacc.yacc(method="SLR")
yacc.yacc()
