FrontEnd:
	AST.py - stores an Abstract Syntax Tree and generates three address code
	lexer.py - Python Lex code for defining tokens
	parser.py - Python Yacc code that defines grammar
	parser.out - Generates a DFA
	parsetab.py - Auto-generated file
BackEnd:
	backend_lexer.py - Python Lex code for defining backend tokens
	backend_parser.py - Python Yacc code that defines backend grammar
	parser.out - Generates a DFA
	mult_div.asm - Code that supports multiplication and division in ARM
	parsetab.py - Auto-generated file

Change log:
(9/09/19) Starter code
(9/11/19) Added multi-digit numbers, comments (single and multi-line), and line number tracking through t.lineno.
(10/8/19) Added AST.py, lexer.py, and parser.py; wordScanner.py removed.
(10/8/19) Updated parser.py to use symbol table to manage variable declarations.
(10/24/19) Added support for subtraction, division and several comparison operators (==,!=,<,>,<=,>=) along with a comp level in the parser.
(10/27/19) Added UnaryOpNode class in AST.py, along with unary minus and unary not (!) of which the class supports.
(11/11/19) Added if-else statements and while loops. Updated AST.py to include three new nodes to support this, as well as a few new stmt grammar rules.
(11/13/19) Fixed issue with grammar in that == and != had same precedence as other comparison operators.
(11/13/19) Added starter backend files into project, added grammar for modulo (added it as a token earlier but forgot to implement it). Put backend and frontend into seperate files. Updated README to include the added files.
(11/25/19) Added code to the backend; now works with all current frontend grammar.
