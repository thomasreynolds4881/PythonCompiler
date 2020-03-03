'''
File: AST.py

This is code for storing an abstract syntax tree (AST) for a small C-like language.
The AST has code for generating three address code in the gen() function of each node.
This is used in the Drake University Compiler Construction course (CS 161).

Author: Eric D. Manley, Thomas Reynolds

Last Updated: 8/21/2019

'''

#this is an auxilliary class meant to be used in a static way
#to generate unique variable and label names that can be used
#in the three address code
class NameGenerator:
	temp_num = 0 #number of temporary variables created
	label_num = 0 #number of temporary labels created

	#generates new temporary variable names of the form
	# _t0, _t1, _t2, etc.
	@staticmethod
	def new_temp():
		temp_name = '_t'+str(NameGenerator.temp_num)
		NameGenerator.temp_num += 1
		return temp_name

	#generates new label names of the form
	# L0, L1, L2, etc.
	@staticmethod
	def new_label():
		label_name = 'L'+str(NameGenerator.label_num)
		NameGenerator.label_num += 1
		return label_name




#abstract class with a function
#for generating code
class ASTNode:

        #subclasses will override gen() if they need to generate code
	def gen(self):
		pass

#Representing expressions
#expressions result in a value, and whatever value is computed needs to be stored
#in some variable - which is kept track of in self.__addr
class ExprNode(ASTNode):

	def __init__(self):
		ASTNode.__init__(self)
		#all expressions result in a value which is stored in an address 
		#specified by this string
		self.__addr = ""

	def get_addr(self):
		return self.__addr

	def set_addr(self,a):
		self.__addr = a


#Represents binary operators
class BinaryOpNode(ExprNode):
	def __init__(self, o, l, r):
		ExprNode.__init__(self)
		self.__op = o    #the operator
		self.__left = l  #the left operand
		self.__right = r #the right operand

	def gen(self):
		self.__left.gen() #generate left child tree's code and save the result variable
		self.__right.gen() #generate right child tree's code and save the result variable
		#generate a new temporary variable for placing the result of this ASTNode
		self.set_addr( NameGenerator.new_temp() ) 
		#emit the three address code
		print(self.get_addr(),'=',self.__left.get_addr(),self.__op,self.__right.get_addr())

#Unary op nodes allow negative numbers and using the not operator
class UnaryOpNode(ExprNode):

	def __init__(self, o, exp):
		ExprNode.__init__(self)
		self.__op = o
		self.__expr = exp

	def gen(self):
		self.__expr.gen()
		self.set_addr( NameGenerator.new_temp() ) 
		#emit the three address code
		print(self.get_addr(),'=',self.__op,self.__expr.get_addr())

#Leaf nodes just need to keep track of an address where the value is stored
class LeafNode(ExprNode):

	def __init__(self, a):
		ExprNode.__init__(self)
		self.set_addr(a)

#Assignment statement nodes keep track of the expression to evaluate
# and the variable to assign the result to
class AssignNode(ASTNode):

	def __init__(self,varname,exp):
		ASTNode.__init__(self)
		self.__var = varname #left hand side of assignment statement
		self.__expr = exp    #right hand side of assignment statement

	def gen(self):
		self.__expr.gen() #generate code for the value we're assigning
		#three address code for assigning the value to the rhs ID
		print(self.__var,'=',self.__expr.get_addr())

#read statements specify an address to read into
class ReadNode(ASTNode):

	def __init__(self,l):
		ASTNode.__init__(self)
		self.__addr_to_read_into = l

	def gen(self):
		print('read',self.__addr_to_read_into)

#write statements can output any arbitrary expression
class WriteNode(ASTNode):

	def __init__(self,exp):
		ASTNode.__init__(self)
		self.__thing_to_output = exp #the expression to evaluate and output

	def gen(self):
		self.__thing_to_output.gen() #generate code for the expression we're outputting
		print('write',self.__thing_to_output.get_addr())

class IfNode(ExprNode):

	def __init__(self,exp,stmt):
		ExprNode.__init__(self)
		self.__expr = exp
		self.__stmt = stmt

	def gen(self):
		self.__expr.gen()
		self.set_addr( NameGenerator.new_label() )
		print("ifFalse", self.__expr.get_addr(), "goto",self.get_addr())
		self.__stmt.gen()
		print(self.get_addr()+':')

class IfElseNode(ExprNode):

	def __init__(self,exp,stmt1,stmt2):
		ExprNode.__init__(self)
		self.__expr = exp
		self.__stmt1 = stmt1
		self.__stmt2 = stmt2

	def gen(self):
		self.__expr.gen()
		label0 = NameGenerator.new_label() #label 1
		label1 = NameGenerator.new_label() #label 2
		print("ifFalse", self.__expr.get_addr(), "goto", label0)
		self.__stmt1.gen()
		print("goto", label1)
		print(label0+':')
		self.__stmt2.gen()
		print(label1+':')

class WhileNode(ExprNode):

	def __init__(self,exp,stmt):
		ExprNode.__init__(self)
		self.__expr = exp
		self.__stmt = stmt

	def gen(self):
		label0 = NameGenerator.new_label()
		label1 = NameGenerator.new_label()
		print(label0+':')
		self.__expr.gen()
		print("ifFalse", self.__expr.get_addr(), "goto", label1)
		self.__stmt.gen()
		print("goto", label0)
		print(label1+':')


#Sequence nodes allow the tree to have any number of consecutive statments,
#represented in this tree as a series of binary nodes that can each be a SeqNode or a statement
class SeqNode(ASTNode):

	def __init__(self,l,r):
		ASTNode.__init__(self)
		self.__first = l
		self.__second = r

	def gen(self):
		#only try to call gen() if the child node is not None
		if self.__first:
			self.__first.gen() #generate code for the left branch first
		if self.__second:
			self.__second.gen() #generate code for the right branch second