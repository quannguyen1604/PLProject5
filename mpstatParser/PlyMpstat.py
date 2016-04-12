tokens = ('COLUMN', 'INTEGER')
literals = [':', '.', ',', "-"]

# Tokens
t_COLUMN   = r'[A-Z][ -~]+'



def t_INTEGER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " \r\n"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex   # ply.lex comes from the ply folder in the PLY download.
lexer = lex.lex()

# Parsing rules

global time_step
time_step = 0

def p_start(t):
    '''start : column
             | data
    '''


def p_column(t):
    'column : COLUMN '
    print "CREATE TABLE 'IBMStockPrice' (Date date, Open varchar(255),High varchar(255),Low varchar(255),Close varchar(255),Volume varchar(255),AdjClose varchar(255));"


def p_data(t):
    'data : INTEGER "-" INTEGER "-" INTEGER "," float "," float "," float "," float "," INTEGER "," float'
    print "INSERT INTO IBMStockPrice (Date,Open,High,Low,Close,Volume,AdjClose) values(" + str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6]) + str(t[7]) + str(t[8]) + str(t[9]) + str(t[10]) + str(t[11]) + str(t[12]) + str(t[13]) + str(t[14]) + str(t[15]) + str(t[16]) + str(t[17]) +");"

def p_float(t):
    'float : INTEGER "." INTEGER'
    t[0] =  str(t[1]) + str(t[2]) + str(t[3])

def p_error(t):
    if t == None:
        print("Syntax error at '%s'" % t)
    else:
        print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc   # ply.yacc comes from the ply folder in the PLY download.
parser = yacc.yacc()

while True:
    try:
        s = raw_input('')
    except EOFError:
        break
    parser.parse(s)

    # To run the parser do the following in a terminal window: head -30 plyParserInputs/table.csv | grep -v '^\s*$' | python PlyMpstat.py | sed "s/_~_/1, 9999, 2,/"