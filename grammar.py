'''
ESCUELA DE VACACIONES JUNIO 2021
GRAMATICA PROYECTO COMPILADORES 1 
ALUMNO ESTRELLA: JAMES OSMIN GRAMAJO CARCAMO
CARNÉ: 201731172
USAC
'''

tokens=(
    'VAR',
    'TRUE',
    'FALSE',
    'COMILLAS',
    'COMILLASIMPLE',
    'ESPCOMILLAS',
    'ESPCOMILLASIMPLE',
    'ESPBARRAINVERTIVA',
    'ESPLINEA',
    'ESPRETORNO',
    'ESPTAB',
    'NULL',
    'MAS',
    'MENOS',
    'POR',
    'DIV',
    'POT',
    'MODULO',
    'IGUAL',
    'IGUALACION',
    'DECIMAL',
    'ENTERO',
    'CHART',
    'DIREFENCIACION',
    'MENORQ',
    'MAYORQ',
    'MENORIGUAL',
    'MAYORIGUAL',
    ##OPERADOR LOGICO
    'OR',
    'AND',
    'NOT',
    'HOLA',
    #ENCAPSULACION
    'PTCOMA',
    'DOSPUNTOS',
    'CORCHETE_ABRE',
    'CORCHETE_CIERRA',
    'LLAVE_ABRE',
    'LLAVE_CIERRA',
    'PARENTESIS_ABRE',
    'PARENTESIS_CIERRA',
    #PARA CASTEOS
    'STRING',
    'INT',
    'CHAR',
    'DOUBLE',
    #INCREMENTO Y DECREMENTO
    'INCREMENTO',
    'DECREMENTO',
    'NEW',
    'IF',
    'ELSE',
    'PRINT',
    'SWITCH',
    'CASE',
    'DEFAULT',
    'BREAK',
    'WHILE',
    'FOR',
    'RETURN',
    'FUNC',
    'MAIN',
    'IDENTIFICADOR',
    'READ',
    'TOLOWER',
    'TOUPPER',
    'LENGTH',
    'CADENA'
)
states = (
  ('COMENTARIOBLOQU','exclusive'),
)

#tokens
t_VAR=              r'[Vv][Aa][Rr]'
t_HOLA=             r'[H][O][L][A]'
t_TRUE=             r'[Tt][Rr][Uu][Ee]'
t_FALSE=            r'[Ff][Aa][Ll][Ss][Ee]'
t_COMILLAS=         r'[\"]'
t_COMILLASIMPLE=    r'[\']'
t_ESPCOMILLAS=      r'[\\][\"]'
t_ESPCOMILLASIMPLE= r'[\\][\']'
t_ESPBARRAINVERTIVA=r'[\\]'
t_ESPLINEA=         r'[\\][n]'
t_ESPRETORNO=       r'[\\][r]'
t_ESPTAB=           r'[\\][t]'
t_NULL=             r'[Nn][Uu][Ll][Ll]'
t_MAS=              r'\+'
t_MENOS=            r'-'
t_POR=              r'\*'
t_DIV=              r'/'
t_POT=              r'\*\*'
t_MODULO=           r'\%'
#OPERADORES RELACIONALES
t_IGUAL=            r'='
t_IGUALACION=       r'[=][=]'
t_DIREFENCIACION=   r'=!'
t_MENORQ=           r'<'
t_MAYORQ=           r'>'
t_MENORIGUAL=       r'<='
t_MAYORIGUAL=       r'>='
#OPERADOR LOGICO
t_AND=              r'&&'
t_OR=               r'\|\|'
t_NOT=              r'!'
#ENCAPSULACION
t_PTCOMA=           r';'
t_DOSPUNTOS=        r':'
t_CORCHETE_ABRE=    r'\['
t_CORCHETE_CIERRA=  r'\]'
t_LLAVE_ABRE=       r'\{'
t_LLAVE_CIERRA=     r'\}'
t_PARENTESIS_ABRE=  r'\('
t_PARENTESIS_CIERRA=r'\)'
#tokens en casteos
t_INT=              r'[Ii][Nn][Tt]'
t_DOUBLE=           r'[Dd][Oo][Uu][Bb][Ll][Ee]'
t_STRING=           r'[Ss][Tt][Rr][Ii][Nn][Gg]'
t_CHAR=             r'[Cc][Hh][Aa][Rr]'
t_INCREMENTO=       r'[\+][\+]'
t_DECREMENTO=       r'[\-][\-]'
t_NEW=              r'[Nn][Ee][Ww]'
t_ELSE=             r'[Ee][Ll][Ss][Ee]'
t_PRINT=            r'[Pp][Rr][Ii][Nn][Tt]'
t_SWITCH=           r'[Ss][Ww][Ii][Tt][Cc][Hh]'
t_CASE=             r'[Cc][Aa][Ss][Ee]'
t_DEFAULT=          r'[Dd][Ee][Ff][Aa][Uu][Ll][Tt]'
t_BREAK=            r'[Bb][Rr][Ee][Aa][Kk]'
t_WHILE=            r'[Ww][Hh][Ii][Ll][Ee]'
t_FOR=              r'[Ff][Oo][Rr]'
t_RETURN=           r'[Rr][Ee][Tt][Uu][Rr][Nn]'
t_FUNC=             r'[Ff][Uu][Nn][Cc]'
t_IDENTIFICADOR=    r'[A-Z_-z0-9]+'
t_MAIN=             r'[Mm][Aa][Ii][Nn]'
t_IF=               r'[I][F]|[i][f]|[I][f]|[i][F]'
t_READ=             r'[Rr][Ee][Aa][Dd]'
t_TOLOWER=          r'[Tt][Oo][Ll][Oo][Ww][Ee][Rr]'
t_TOUPPER=          r'[Tt][Oo][Uu][Pp][Pp][Ee][Rr]'


def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("El valor es demasiado grande '%d'" % t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large '%d'" % t.value)
        t.value = 0
    return t

def t_begin_COMENTARIOBLOQU(t):
    r'[\#][\*]'
    print('entra')
    t.lexer.begin('COMENTARIOBLOQU')             # Starts 'COMENTARIOBLOQU' state

def t_COMENTARIOBLOQU_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_COMENTARIOBLOQU_LETRAS(t):
    r'[^\*\#]'
    return None

def t_COMENTARIOBLOQU_end(t):
    r'\*\#'
    print('sale')
    t.lexer.begin('INITIAL')


def t_COMENTARIO(t):
    r'[\#][^\n]+'
    print('Comment Line')
    return None

def t_CADENA(t):
    r'(\".*?\")'
    t.value = t.value[1:-1] # remuevo las comillas
    return t

def t_CHART(t):
    r'(\'([(-Za-z#-&]|([\n]|[\t]|[\r]|[\\][\\]|[\\][\']|[\\][\"]|[\{]|[\}]|[\|]|[\!]|[\_]))\')'
    t.value = t.value[1:-1] # remuevo las comillas
    
    return t

##def t_CHART(t):
    ##r'[#-&(-\[a-\}]'
    ##return t

# Caracteres ignorados
t_ignore = " \t"
t_COMENTARIOBLOQU_ignore = "\r\t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t): #LEXICOS
    print('caracter no reconocido: ' + str(t.value[0]))
    # almacenamiento de errores lexicos
    t.lexer.skip(1)

def t_COMENTARIOBLOQU_error(t): #LEXICOS
    #print('caracter no reconocido  ' + str(t.value[0]))
    # almacenamiento de errores lexicos
    t.lexer.skip(1)

    # Construyendo el analizador lexico
import ply.lex as lex
lexer = lex.lex()

# Presedencia
# Presedencia
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOTT'),
    ('left', 'IGUALACION', 'DIREFENCIACION', 'MENORQ', 'MENORIGUAL', 'MAYORQ', 'MAYORIGUAL'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'DIV', 'POR','MODULO'),
    ('left', 'POT'),
    ('right', 'UMENOS')
)
# Definicion de la gramatica
def p_inicio(t):
    '''
    instrucciones : instruccion

    '''

def p_main(t):
    '''
    instruccion : MAIN PARENTESIS_ABRE PARENTESIS_CIERRA LLAVE_ABRE bloque LLAVE_CIERRA
    '''
def p_declaraciones(t):
    '''
    bloque : variables bloque
            | variables
            | if bloque
            | if
            | ifelse bloque
            | ifelse
            | difelseif bloque
            | difelseif
            | switch bloque
            | switch
            | while bloque 
            | while
            | for bloque
            | for


            
    '''

def p_variables(t):
    '''
    variables : VAR IDENTIFICADOR finInstruccion
                | VAR IDENTIFICADOR  IGUAL expresion  finInstruccion
                | IDENTIFICADOR IGUAL expresion finInstruccion
                | IDENTIFICADOR IGUAL incremento finInstruccion
                
    ''' 
def p_incrementos(t):
    '''
    incremento : INCREMENTO
                | DECREMENTO
    '''   
def p_expresion_binaria(t):
    '''
    expresion : expresion MAS expresion
            | expresion MENOS expresion
            | expresion POR expresion
            | expresion DIV expresion
            | expresion POT  expresion
            | expresion MODULO expresion
            | expresion IGUALACION expresion
            | expresion DIREFENCIACION expresion
            | expresion MAYORQ expresion
            | expresion MENORQ expresion
            | expresion MAYORIGUAL expresion
            | expresion MENORIGUAL expresion        
    ''' 
def p_expresion_unaria(t):
    '''
    expresion : MENOS expresion %prec UMENOS
                | NOT expresionl %prec NOTT

    '''

def p_expresion_primitivo(t):
    '''
    expresion : ENTERO
            | DECIMAL
            | TRUE
            | FALSE
            | IDENTIFICADOR
            | CADENA
            | CHART
    '''

def p_expresion_logicap(t):
    '''
    expresionl :  TRUE
                | FALSE
                | IDENTIFICADOR
    '''

def p_if1(t):
    '''
    if : IF PARENTESIS_ABRE condiciones PARENTESIS_CIERRA LLAVE_ABRE LLAVE_CIERRA  
    '''

def p_condicionif(t):
    '''
        condiciones : condiciones IGUALACION condiciones
                    | condiciones DIREFENCIACION condiciones
                    | condiciones MAYORQ condiciones
                    | condiciones MENORQ condiciones
                    | condiciones MAYORIGUAL condiciones
                    | condiciones MENORIGUAL condiciones
                    | condiciones AND condiciones
                    | condiciones OR condiciones
                    | condiciones MAS condiciones
                    | condiciones MENOS condiciones
                    | condiciones POR condiciones
                    | condiciones DIV condiciones
                    | condiciones POT  condiciones
                    | condiciones MODULO condiciones


                    
    '''
def p_expresion_unarialog(t):
    '''
    condiciones : NOT expresionll %prec NOTT
                | MENOS expresion %prec UMENOS

    '''
def p_expresion_agrupacion(t):
    '''
    condiciones : PARENTESIS_ABRE condiciones PARENTESIS_CIERRA
    '''

def p_expresion_logicall(t):
    '''
    expresionll :  TRUE
                | FALSE
                | IDENTIFICADOR

    '''
def p_condicionif2(t):
    '''
    condiciones : ENTERO
            | DECIMAL
            | TRUE
            | FALSE
            | IDENTIFICADOR
            | CADENA
            | CHART
    '''
def p_ifelse(t):
    '''
    ifelse : if else
    '''
def p_else(t):
    '''
    else : ELSE LLAVE_ABRE LLAVE_CIERRA
    '''
def p_difelseif(t):
    '''
    difelseif : if elseif
                
    '''
def p_els(t):
    '''
    elseif : ELSE IF PARENTESIS_ABRE condiciones PARENTESIS_CIERRA LLAVE_ABRE LLAVE_CIERRA elseif
            | ELSE IF PARENTESIS_ABRE condiciones PARENTESIS_CIERRA LLAVE_ABRE LLAVE_CIERRA else
            | ELSE IF PARENTESIS_ABRE condiciones PARENTESIS_CIERRA LLAVE_ABRE LLAVE_CIERRA 
    '''
def p_switch(t):
    '''
    switch : SWITCH PARENTESIS_ABRE expresion PARENTESIS_CIERRA LLAVE_ABRE cases LLAVE_CIERRA
    '''
def p_cases(t):
    '''
    cases : CASE expresion DOSPUNTOS break cases
            | CASE expresion DOSPUNTOS break default
    '''
def p_default(t):
    '''
    default : DEFAULT DOSPUNTOS break
    '''
def p_while(t):
    '''
    while : WHILE PARENTESIS_ABRE expresion PARENTESIS_CIERRA LLAVE_ABRE  LLAVE_CIERRA
    '''
def p_for(t):
    '''
    for : FOR PARENTESIS_ABRE condicionfor PARENTESIS_CIERRA  LLAVE_ABRE  LLAVE_CIERRA
    '''
def p_forcondiciones(t):
    '''
    condicionfor : declaracionfor PTCOMA condiciones PTCOMA actualizacion
    '''
def p_declaracionfor(t):
    '''
    declaracionfor : VAR IDENTIFICADOR  IGUAL expresion  
                | IDENTIFICADOR IGUAL expresion 
                | expresion 
    '''
def p_actualizacionfor(t):
    '''
    actualizacion : IDENTIFICADOR incremento
                    | IDENTIFICADOR IGUAL expresion
    '''

def p_break(t):
    '''
    break : BREAK finInstruccion
            | 
    '''
def p_finInstruccion(t):
    '''
    finInstruccion : PTCOMA
                    |
    '''

def p_error(t):
    print('Error sintactico en: ' + str(t.value)+' Linea '+str(t.lineno))
    # almacenamiento de errores sintacticos

import ply.yacc as yacc
parser = yacc.yacc()

f = open("./entradaa.txt", "r")
input = f.read()
#print(input)
parser.parse(input)
print("Archivo ejecutado correctamente :D")

