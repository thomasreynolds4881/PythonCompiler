'''
File: parser.py

This is Python Yacc code defining the grammar for a small C-like language
used in the Drake University Compiler Construction course (CS 161)

Author: Eric D. Manley, Luke Gentle, Thomas Reynolds
Sources: https://ruslanspivak.com/lsbasi-part8/

Last Updated: 8/21/2019

'''
import ply.yacc as yacc
from lexer import tokens #the lexer we wrote
import sys
import AST #abstract syntax tree we wrote


'''
***Here is the full grammar***
program : block

block : LBRACE stmt_list RBRACE

stmt_list : stmt_list stmt
stmt_list : 

stmt : type ID SEMICOLON
stmt : ID ASSIGN logicor SEMICOLON
stmt : block
stmt : READ ID SEMICOLON
stmt : WRITE logicor SEMICOLON
stmt : IF LPAREN logicor RPAREN block
stmt : IF LPAREN logicor RPAREN block ELSE block
stmt : WHILE LPAREN logicor RPAREN block

else : block
else : 

type : INT

logicor : logicor OR logicand
logicor : logicand

logicand : logicand AND compEq
logicand : compEq

compEq : compEq EQUALTO comp
compEq : compEq NOTEQUALTO comp
compEq : comp

comp : comp LESSTHAN expr
comp : comp LESSEQUALTO expr
comp : comp GREATERTHAN expr
comp : comp GREATEREQUALTO expr
comp : comp EQUALTO expr
comp : comp NOTEQUALTO expr
comp : expr

expr : expr PLUS term
expr : expr MINUS term
expr : term

term : term TIMES factor
term : term DIVIDE factor
term : term MODULO factor
term : factor

factor : ID
factor : NUM
factor : MINUS factor
factor : LPAREN logicor RPAREN

'''

#Each production in the grammar gets a function describing
#what to do when that rule is used in parsing

#program is the top-level symbol, for now defined as a single
#block of code. Once we have the full AST built, we call the
#gen() function on the root which will recursively emit the
#three address code for the entire tree

symbol_table_list = []

def p_program(p):
	'''
	program : block
	'''
	p[0] = p[1]
	p[0].gen()

def p_block(p):
	'''
	block : LBRACE action_new_scope stmt_list RBRACE
	'''
	p[0] = p[3]
	symbol_table_list.pop(0)

def p_action_new_scope(p):
	'''
	action_new_scope : 
	'''
	global symbol_table_list
	new_symbol_table = {}
	symbol_table_list.insert(0,new_symbol_table)

#sequence nodes allow statements to be executed
#one after another
def p_stmt_list(p):
	'''
	stmt_list : stmt_list stmt
	'''
	p[0] = AST.SeqNode(p[1],p[2])

#a statement list can be empty, if so we have a
#termoinal spot in the AST represented by None
def p_stmt_list_empty(p):
	'''
	stmt_list : 
	'''
	p[0] = None

#declaration statements - the language doesn't do
#anything with this other than parse them
def p_stmt_decl(p):
	'''
	stmt : type ID SEMICOLON
	'''
	global symbol_table_list
	curr_symbol_table = symbol_table_list[0]
	for curr_symbol_table in symbol_table_list:
		if p[2] in curr_symbol_table:
			print("Error: duplicate ID name")
			return
	curr_symbol_table[p[2]] = (p[1],'line '+str(p.lineno(2)))
	p[0] = None #we don't need to include declarations in the tree yet

#assignment statements get assignment nodes
def p_stmt_assign(p):
	'''
    stmt : ID ASSIGN expr SEMICOLON
	'''
	for curr_symbol_table in symbol_table_list:
		if p[1] in curr_symbol_table:
			p[0] = AST.AssignNode(p[1],p[3])
			return
	print("Error: ID not found")
	p[0] = None

#blocks just get passed up the tree
def p_stmt_block(p):
	'''
	stmt : block
	'''
	p[0] = p[1]

#read statements get read nodes
def p_stmt_read(p):
	'''
	stmt : READ ID SEMICOLON
	'''
	for curr_symbol_table in symbol_table_list:
		if p[2] in curr_symbol_table:
			p[0] = AST.ReadNode(p[2])
			return
	print("Error: ID not found")

#write statements get write nodes
def p_stmt_write(p):
	'''
	stmt : WRITE logicor SEMICOLON
	'''
	p[0] = AST.WriteNode(p[2])

def p_stmt_if(p):
	'''
	stmt : IF LPAREN logicor RPAREN block
	'''
	p[0] = AST.IfNode(p[3], p[5])

def p_stmt_if_else(p):
	'''
	stmt : IF LPAREN logicor RPAREN block ELSE block
	'''
	p[0] = AST.IfElseNode(p[3], p[5], p[7])

def p_while(p):
	'''
	stmt : WHILE LPAREN logicor RPAREN block
	'''
	p[0] = AST.WhileNode(p[3],p[5])

#we're not doing anything with types yet
def p_type(p):
	'''
	type : INT
	'''
	pass

def p_logicor_logicor(p):
	'''
	logicor : logicor OR logicand
	'''
	p[0] = AST.BinaryOpNode(p[2],p[1],p[3])

def p_logicor_logicand(p):
	'''
	logicor : logicand
	'''
	p[0] = p[1]

def p_logicand_logicand(p):
	'''
	logicand : logicand AND compEq
	'''
	p[0] = AST.BinaryOpNode(p[2],p[1],p[3])

def p_logicand_compEq(p):
	'''
	logicand : compEq
	'''
	p[0] = p[1]

def p_compEq_equal(p):
	'''
	compEq : compEq EQUALTO comp
	'''
	p[0] = AST.BinaryOpNode(p[2],p[1],p[3])

def p_compEq_notequal(p):
	'''
	compEq : compEq NOTEQUALTO comp
	'''
	p[0] = AST.BinaryOpNode(p[2],p[1],p[3])

def p_compEq_comp(p):
	'''
	compEq : comp
	'''
	p[0] = p[1]

def p_comp_less(p):
	'''
	comp : comp LESSTHAN expr
	'''
	p[0] = AST.BinaryOpNode(p[2],p[1],p[3])

def p_comp_lessequal(p):
	'''
	comp : comp LESSEQUALTO expr
	'''
	p[0] = AST.BinaryOpNode(p[2],p[1],p[3])

def p_comp_greater(p):
	'''
	comp : comp GREATERTHAN expr
	'''
	p[0] = AST.BinaryOpNode(p[2],p[1],p[3])

def p_comp_greaterequal(p):
	'''
	comp : comp GREATEREQUALTO expr
	'''
	p[0] = AST.BinaryOpNode(p[2],p[1],p[3])

def p_comp_compEq(p):
	'''
	comp : expr
	'''
	p[0] = p[1]

#expression with the + and - operator are represented
#with a binary operator node in the AST
def p_expr_plus(p):
	'''
	expr : expr PLUS term
	'''
	p[0] = AST.BinaryOpNode(p[2],p[1],p[3])

def p_expr_minus(p):
	'''
	expr : expr MINUS term
	'''
	p[0] = AST.BinaryOpNode(p[2],p[1],p[3])

def p_expr_term(p):
	'''
	expr : term
	'''
	p[0] = p[1]

#expression with the * and / operator are represented
#with a binary operator node in the AST
def p_term_times(p):
	'''
	term : term TIMES factor
	'''
	p[0] = AST.BinaryOpNode(p[2],p[1],p[3])

def p_term_divide(p):
	'''
	term : term DIVIDE factor
	'''
	p[0] = AST.BinaryOpNode(p[2],p[1],p[3])

def p_term_modulo(p):
	'''
	term : term MODULO factor
	'''
	p[0] = AST.BinaryOpNode(p[2],p[1],p[3])

def p_term_factor(p):
	'''
	term : factor
	'''
	p[0] = p[1]

def p_factor_minus(p):
	'''
	factor : MINUS factor
	'''
	p[0] = AST.UnaryOpNode(p[1],p[2])

def p_factor_not(p):
	'''
	factor : NOT factor
	'''
	p[0] = AST.UnaryOpNode(p[1],p[2])

#we only need the value passed by the lexer
#to create a leaf node with an ID
def p_factor_id(p):
	'''
	factor : ID
	'''
	for curr_symbol_table in symbol_table_list:
		if p[1] in curr_symbol_table:
			p[0] = AST.LeafNode(p[1])
			return
	print("Error: ID not found")

#we only need the value passed by the lexer (which was converted to an int)
#to create a leaf node with a NUM
def p_factor_num(p):
	'''
	factor : NUM
	'''
	p[0] = AST.LeafNode(p[1])

#parenthetical statements can be passed up the tree
def p_factor_parens(p):
	'''
	factor : LPAREN logicor RPAREN
	'''
	p[0] = p[2]


# Error rule for syntax errors
def p_error(p):
	print("Syntax error in input at line",p.lineno,p)

# Build the parser
parser = yacc.yacc()
#parse the string from standard in
#stop at the EOF character
parser.parse(sys.stdin.read())



