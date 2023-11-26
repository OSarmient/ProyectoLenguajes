import ply.yacc as yacc
from lexer import tokens  # Asegúrate de importar los tokens del lexer

# Definición de las reglas del parser

def p_expression_plus(p):
    'expression : expression PLUS term'
    # Implementar la lógica aquí

def p_expression_term(p):
    'expression : term'
    # Implementar la lógica aquí

def p_term_times(p):
    'term : term TIMES factor'
    # Implementar la lógica aquí

def p_term_factor(p):
    'term : factor'
    # Implementar la lógica aquí

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_error(p):
    print(f"Syntax error at '{p.value}'")

# Construir el parser
parser = yacc.yacc()
