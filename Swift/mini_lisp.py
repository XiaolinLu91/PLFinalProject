# -*- coding: utf-8 -*-

from yacc import yacc


vars = {}
constants = {}

def bool_func(first, oper, second):
    if oper == "==":
        return first == second
    elif oper == "!=":
        return first != second
    elif oper == ">":
        return first > second
    elif oper == "<":
        return first < second
    elif oper == ">=":
        return first >= second
    elif oper == "<=":
        return first <= second

def eval_ast(ast):
    for instrs in ast:
        if instrs[0] == 'var':
            if instrs[1] not in vars: 
                vars[instrs[1]] = instrs[2]
                if isinstance(instrs[2], (list)) and instrs[2][0] == 'arithmetic':
                    vars[instrs[1]] = eval("".join(str(x) for x in instrs[2][1:]))
            else:
                raise Exception("Variable already defined")

        elif instrs[0] == 'let':
            if instrs[1] not in constants: 
                constants[instrs[1]] = instrs[2]
                if isinstance(instrs[2], (list)) and instrs[2][0] == 'arithmetic': 
                    constants[instrs[1]] = eval("".join(str(x) for x in instrs[2][1:]))
            else:
                raise Exception("Cannot change a constant")

        elif instrs[0] == 'print':
            if instrs[1] == "": 
                print ""
            elif instrs[1] in vars: 
                print vars[instrs[1]]
            elif instrs[1] in constants: 
                print constants[instrs[1]]
            elif isinstance(instrs[1], (int, float)): 
                print instrs[1]
            elif instrs[1][0] == '"' and instrs[1][-1] == '"': 
                print instrs[1][1:-1]
            else: 
                raise Exception("No such variable " + instrs[1])

        elif instrs[0] == 'arithmetic':
            print(eval("".join(str(x) for x in instrs[1:]))) 

        elif instrs[0] == 'reduce':
            if instrs[1] in constants: 
                raise Exception("Cannot change a constant")
            elif instrs[1] in vars:
                if instrs[2] == "=" and isinstance(instrs[3], (int, float)): 
                    vars[instrs[1]] = instrs[3]
                elif instrs[2] == "+=":
                    vars[instrs[1]] = vars[instrs[1]] + float(instrs[3])
                elif instrs[2] == "-=":
                    vars[instrs[1]] = vars[instrs[1]] - float(instrs[3])
                elif instrs[2] == "*=":
                    vars[instrs[1]] = vars[instrs[1]] * float(instrs[3])
                elif instrs[2] == "/=":
                    vars[instrs[1]] = vars[instrs[1]] / float(instrs[3])
                else: 
                    vars[instrs[1]] = eval("".join(str(x) for x in instrs[3][1:]))
            else:
                raise Exception("Variable " + instrs[1] + " not defined")

        elif instrs[0] == 'if':
            if instrs[1][0] in vars and isinstance(instrs[1][2], (int, float)): 
                if bool_func(vars[instrs[1][0]], instrs[1][1], instrs[1][2]): 
                    eval_ast(instrs[2]) 
                elif len(instrs) == 4: 
                    eval_ast(instrs[3][1])
            elif isinstance(instrs[1][0], (int, float)) and instrs[1][2] in vars: 
                if bool_func(instrs[1][0], instrs[1][1], vars[instrs[1][2]]): 
                    eval_ast(instrs[2]) 
                elif len(instrs) == 4: 
                    eval_ast(instrs[3][1])
            elif instrs[1][0] in constants and isinstance(instrs[1][2], (int, float)): 
                if bool_func(constants[instrs[1][0]], instrs[1][1], instrs[1][2]): 
                    eval_ast(instrs[2]) 
                elif len(instrs) == 4: 
                    eval_ast(instrs[3][1])
            elif isinstance(instrs[1][0], (int, float)) and instrs[1][2] in constants: 
                if bool_func(instrs[1][0], instrs[1][1], constants[instrs[1][2]]): 
                    eval_ast(instrs[2]) 
                elif len(instrs) == 4: 
                    eval_ast(instrs[3][1])
            elif isinstance(instrs[1][0], (int, float)) and isinstance(instrs[1][0], (int, float)): 
                if bool_func(instrs[1][0], instrs[1][1], instrs[1][2]): 
                    eval_ast(instrs[2]) 
                elif len(instrs) == 4: 
                    eval_ast(instrs[3][1])
            elif instrs[1][0] in vars and isinstance(instrs[1][2], (str)): 
                if bool_func(vars[instrs[1][0]], instrs[1][1], instrs[1][2]):
                    eval_ast(instrs[2]) 
                elif len(instrs) == 4: 
                    eval_ast(instrs[3][1])
            elif instrs[1][0] in constants and isinstance(instrs[1][2], (str)): 
                if bool_func(constants[instrs[1][0]], instrs[1][1], instrs[1][2]): 
                    eval_ast(instrs[2]) 
                elif len(instrs) == 4: 
                    eval_ast(instrs[3][1])
            else:
                raise Exception("Symbol not found")

with open('test_program.swift', 'r') as swift_file:
    content = swift_file.read()
swift_file.close()
ast = yacc.parse(content)

print "ast: " + str(ast)
eval_ast(ast)
vars.clear()
constants.clear()
print("\n\n")
