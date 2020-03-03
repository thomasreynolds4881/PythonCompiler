'''
File: backendLexer.py

This is Python Lex code defining tokens for the intermediate three address code
used in the Drake University Compiler Construction course (CS 161)

Author: Eric D. Manley, Thomas Reynolds

Last Updated: 11/4/2019

'''
import ply.lex as lex

#a dictionary mapping reserved word lexemes to token names
reserved = {
	'read' : 'READ',
	'write' : 'WRITE',
	'ifFalse' : 'IFFALSE',
	'ifTrue' : 'IFTRUE',
	'goto' : 'GOTO'
}

#this is the list of all tokens in our language
#it includes the reserved words
tokens = [
	'COLON',
	'TIMES',
	'DIVIDE',
	'PLUS',
	'MINUS',
	'ASSIGN',
	'LESSTHAN',
	'GREATERTHAN',
	'LESSEQUALTO',
	'GREATEREQUALTO',
	'EQUALTO',
	'NOTEQUALTO',
	'AND',
	'OR',
	'NOT',
	'NUM',
	'ID'
	]+list(reserved.values())


# Regular expression rules for simple tokens
t_COLON = r':'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_ASSIGN = r'\='
t_LESSTHAN = r'\<'
t_GREATERTHAN = r'\>'
t_LESSEQUALTO = r'\<\='
t_GREATEREQUALTO = r'\>\='
t_EQUALTO = r'\=\='
t_NOTEQUALTO = r'\!\='
t_AND = r'\&\&'
t_OR = r'\|\|'
t_NOT = r'\!'

#matching identifiers - starting with a letter or underscore
#followed by any number of letters, numbers, and underscores
def t_ID(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*'

	#reserved words get their own
	#token type, not ID
	if t.value in reserved:
		t.type = reserved[t.value]

	return t

#this regular expression will match a single digit
def t_NUM(t):
	r'\d+'
	t.value = int(t.value)    
	return t

# A string containing ignored characters (spaces, tabs, and newlines)
t_ignore  = ' \t\n'

def t_error(t):
	print('Illegal character:',t.value[0])
	t.lexer.skip(1)


lexer = lex.lex()
