'''
File: backendParser.py

This is Python Yacc code defining the grammar for three address code
used in the Drake University Compiler Construction course (CS 161) and
compiling it into ARM

Author: Eric D. Manley, Thomas Reynolds

Last Updated: 11/05/2019

'''
import ply.yacc as yacc
from backendLexer import tokens #the lexer we wrote
import sys
import os

#this is used for including the file with
#the multiply and divide procedures
this_directory = os.path.dirname(os.path.abspath(__file__))



'''
***Here is the full grammar***
program : instruction_list label_list

instruction_list : instruction_list instruction
instruction_list :

instruction : label_list three_address_instruction

three_address_instruction : lhs ASSIGN operand
three_address_instruction : lhs ASSIGN operand PLUS operand
three_address_instruction : lhs ASSIGN operand MINUS operand
three_address_instruction : lhs ASSIGN operand TIMES operand
three_address_instruction : lhs ASSIGN operand DIVIDE operand
three_address_instruction : lhs ASSIGN MINUS operand
three_address_instruction : lhs ASSIGN NOT operand
three_address_instruction : lhs operand LESSTHAN operand
three_address_instruction : lhs operand GREATERTHAN operand
three_address_instruction : lhs operand LESSEQUALTO operand
three_address_instruction : lhs operand GREATEREQUALTO operand
three_address_instruction : lhs operand EQUALTO operand
three_address_instruction : lhs operand NOTEQUALTO operand
three_address_instruction : lhs ASSIGN operand AND operand
three_address_instruction : lhs ASSIGN operand OR operand
three_address_instruction : IFFALSE operand GOTO label
three_address_instruction : IFTRUE operand GOTO label
three_address_instruction : GOTO label
three_address_instruction : WRITE operand
three_address_instruction : READ lhs

lhs : ID

label_list : label_list label
label_list :

operand : ID
operand : NUM

label : ID COLON

'''


'''
***Project notes***
This compiler produces ARM assembly code, with memory-mapped input/output.
That means that there are memory locations associated with console input
and output, and so to read and write, you will just load and store values
to these memory locations.

The registers r11 and r12 will keep track of the current location within
the memory block for each of output and input, so don't use them with any
other instruction translations.

'''

class labelGenerator:
        label_num = 0 #number of temporary labels created

        #generates new label names of the form
        # label, L1, L2, etc.
        @staticmethod
        def new_label():
                label_name = 'LAB'+str(labelGenerator.label_num)
                labelGenerator.label_num += 1
                return label_name

#This class will be used as the type for some
#p[0], p[1], etc. when we need to keep track of
#a value and what kind of thing it is (an id vs. a num)
class OperandInfo:
        def __init__(self):
                self.val = ''
                self.kind = ''

variable_set = set() # create an initially empty set to keep track of all the variables we see

#Each production in the grammar gets a function describing
#what to do when that rule is used in parsing


def p_program(p):
        '''
        program : instruction_list label_list
        '''
        pass

def p_instruction_list_instruction(p):
        '''
        instruction_list : instruction_list instruction
        '''
        pass

def p_instruction_list_empty(p):
        '''
        instruction_list :
        '''
        pass

def p_instruction(p):
        '''
        instruction : label_list three_address_instruction
        '''
        pass



def p_three_address_instruction_assign(p):
        '''
        three_address_instruction : lhs ASSIGN operand
        '''
        #r0: address of operand p[3] if it is an id
        #r1: value of operand p[3]
        #r2: address of lhs

        #printing out a comment with a three-address code
        #version of what we're working on
        print('\n\t;',p[1],'=',p[3].val)

        #if it's a num, we don't need to also load the address
        if p[3].kind == 'num':
                print('\t','LDR r1, =',p[3].val,sep='')
        elif p[3].kind == 'id':
                print('\t','LDR r0, =',p[3].val,sep='')
                print('\t','LDR r1, [r0]',sep='')

        print('\t','LDR r2, =',p[1],sep='')
        print('\t','STR r1, [r2]',sep='')
                

def p_three_address_instruction_plus(p):
        '''
        three_address_instruction : lhs ASSIGN operand PLUS operand
        '''
        #r0: address of operand p[3]
        #r1: value of operand p[3]
        #r2: address of operand p[5]
        #r3: value of operand p[5]
        #r4: address of lhs p[1]
        #r5: address of the result to store in lhs p[1]

        #printing out a comment with a three-address code
        #version of what we're working on
        print('\n\t;',p[1],'=',p[3].val,'+',p[5].val)

        #load p[3]
        #if it's a num, we don't need to also load the address
        if p[3].kind == 'num':
                print('\t','LDR r1, =',p[3].val,sep='')
        elif p[3].kind == 'id':
                print('\t','LDR r0, =',p[3].val,sep='')
                print('\t','LDR r1, [r0]',sep='')

        #load p[5]
        #if it's a num, we don't need to also load the address
        if p[5].kind == 'num':
                print('\t','LDR r3, =',p[5].val,sep='')
        elif p[5].kind == 'id':
                print('\t','LDR r2, =',p[5].val,sep='')
                print('\t','LDR r3, [r2]',sep='')

        #load address for lhs p[1]
        print('\t','LDR r4, =',p[1],sep='')

        #perform operation
        print('\t','ADD r5, r1, r3',sep='')

        #store result
        print('\t','STR r5, [r4]',sep='')

def p_three_address_instruction_minus(p):
        '''
        three_address_instruction : lhs ASSIGN operand MINUS operand
        '''
        #r0: address of operand p[3]
        #r1: value of operand p[3]
        #r2: address of operand p[5]
        #r3: value of operand p[5]
        #r4: address of lhs p[1]
        #r5: address of the result to store in lhs p[1]

        #printing out a comment with a three-address code
        #version of what we're working on
        print('\n\t;',p[1],'=',p[3].val,'+',p[5].val)

        #load p[3]
        #if it's a num, we don't need to also load the address
        if p[3].kind == 'num':
                print('\t','LDR r1, =',p[3].val,sep='')
        elif p[3].kind == 'id':
                print('\t','LDR r0, =',p[3].val,sep='')
                print('\t','LDR r1, [r0]',sep='')

        #load p[5]
        #if it's a num, we don't need to also load the address
        if p[5].kind == 'num':
                print('\t','LDR r3, =',p[5].val,sep='')
        elif p[5].kind == 'id':
                print('\t','LDR r2, =',p[5].val,sep='')
                print('\t','LDR r3, [r2]',sep='')

        #load address for lhs p[1]
        print('\t','LDR r4, =',p[1],sep='')

        #perform operation
        print('\t','SUB r5, r1, r3',sep='')

        #store result
        print('\t','STR r5, [r4]',sep='')

def p_three_address_instruction_times(p):
        '''
        three_address_instruction : lhs ASSIGN operand TIMES operand
        '''
        #r2: address of operand p[3]
        #r0: value of operand p[3], later the value returned from
        #  the multiply procedure
        #r3: address of operand p[5]
        #r1: value of operand p[5]
        #r4: address of lhs p[1]

        #printing out a comment with a three-address code
        #version of what we're working on
        print('\n\t;',p[1],'=',p[3].val,'*',p[5].val)

        #load p[3]
        #if it's a num, we don't need to also load the address
        if p[3].kind == 'num':
                print('\t','LDR r0, =',p[3].val,sep='')
        elif p[3].kind == 'id':
                print('\t','LDR r2, =',p[3].val,sep='')
                print('\t','LDR r0, [r2]',sep='')

        #load p[5]
        #if it's a num, we don't need to also load the address
        if p[5].kind == 'num':
                print('\t','LDR r1, =',p[5].val,sep='')
        elif p[5].kind == 'id':
                print('\t','LDR r3, =',p[5].val,sep='')
                print('\t','LDR r1, [r3]',sep='')

        #load address for lhs p[1]
        print('\t','LDR r4, =',p[1],sep='')

        #perform operation, result goes in r0
        print('\t','BL signed_multiply',sep='')

        #store result
        print('\t','STR r0, [r4]',sep='')

def p_three_address_instruction_divide(p):
        '''
        three_address_instruction : lhs ASSIGN operand DIVIDE operand
        '''
        #r2: address of operand p[3]
        #r0: value of operand p[3], later the value returned from
        #  the divide procedure
        #r3: address of operand p[5]
        #r1: value of operand p[5]
        #r4: address of lhs p[1]

        #printing out a comment with a three-address code
        #version of what we're working on
        print('\n\t;',p[1],'=',p[3].val,'*',p[5].val)

        #load p[3]
        #if it's a num, we don't need to also load the address
        if p[3].kind == 'num':
                print('\t','LDR r0, =',p[3].val,sep='')
        elif p[3].kind == 'id':
                print('\t','LDR r2, =',p[3].val,sep='')
                print('\t','LDR r0, [r2]',sep='')

        #load p[5]
        #if it's a num, we don't need to also load the address
        if p[5].kind == 'num':
                print('\t','LDR r1, =',p[5].val,sep='')
        elif p[5].kind == 'id':
                print('\t','LDR r3, =',p[5].val,sep='')
                print('\t','LDR r1, [r3]',sep='')

        #load address for lhs p[1]
        print('\t','LDR r4, =',p[1],sep='')

        #perform operation, result goes in r0
        print('\t','BL signed_divide',sep='')

        #store result
        print('\t','STR r0, [r4]',sep='')

def p_three_address_instruction_unaryminus(p):
        '''
        three_address_instruction : lhs ASSIGN MINUS operand
        '''

        print('\n\t;',p[1],'= -',p[4].val)

        if p[4].kind == 'num':
                print('\t','LDR r0, =',p[4].val,sep='')
        elif p[4].kind == 'id':
                print('\t','LDR r2, =',p[4].val,sep='')
                print('\t','LDR r0, [r2]',sep='')

        print('\t','LDR r4, =0',sep='')
        print('\t','SUB r4, r4, r0',sep='')
        print('\t','LDR r4, =',p[1],sep='')
        print('\t','STR r0, [r4]',sep='')

def p_three_address_instruction_unarynot(p):
        '''
        three_address_instruction : lhs ASSIGN NOT operand
        '''

        print('\n\t;',p[1],'= !',p[4].val)

        if p[4].kind == 'num':
                print('\t','LDR r0, =',p[4].val,sep='')
        elif p[4].kind == 'id':
                print('\t','LDR r2, =',p[4].val,sep='')
                print('\t','LDR r0, [r2]',sep='')

        print('\t','LDR r4, =0',sep='')
        print('\t','CMP r0, #0',sep='')
        print('\t','LDRNE r4, =0',sep='')
        print('\t','LDREQ r4, =1',sep='')
        print('\t','LDR r0, =',p[1],sep='')
        print('\t','STR r4, [r0]',sep='')

def p_three_address_instruction_lessthan(p):
        '''
        three_address_instruction : lhs ASSIGN operand LESSTHAN operand
        '''
        #r2: address of operand p[3]
        #r0: value of operand p[3], later the value returned
        #r3: address of operand p[5]
        #r1: value of operand p[5]
        #r4: address of lhs p[1]

        print('\n\t;',p[1],'=',p[3].val,'<',p[5].val)

        label = labelGenerator.new_label()

        #load p[3]
        #if it's a num, we don't need to also load the address
        if p[3].kind == 'num':
                print('\t','LDR r0, =',p[3].val,sep='')
        elif p[3].kind == 'id':
                print('\t','LDR r2, =',p[3].val,sep='')
                print('\t','LDR r0, [r2]',sep='')

        #load p[5]
        #if it's a num, we don't need to also load the address
        if p[5].kind == 'num':
                print('\t','LDR r1, =',p[5].val,sep='')
        elif p[5].kind == 'id':
                print('\t','LDR r3, =',p[5].val,sep='')
                print('\t','LDR r1, [r3]',sep='')

        print('\t','LDR r4, =1',sep='')
        print('\t','CMP r0, r1',sep='')
        print('\t','BLT ',label,sep='')
        print('\t','LDR r4, =0',sep='')
        print(label)
        print('\t','LDR r5, =',p[1],sep='')
        print('\t','STR r4, [r2]',sep='')

def p_three_address_instruction_greaterthan(p):
        '''
        three_address_instruction : lhs ASSIGN operand GREATERTHAN operand
        '''
        #r2: address of operand p[3]
        #r0: value of operand p[3], later the value returned
        #r3: address of operand p[5]
        #r1: value of operand p[5]
        #r4: address of lhs p[1]

        print('\n\t;',p[1],'=',p[3].val,'<',p[5].val)

        label = labelGenerator.new_label()

        #load p[3]
        #if it's a num, we don't need to also load the address
        if p[3].kind == 'num':
                print('\t','LDR r0, =',p[3].val,sep='')
        elif p[3].kind == 'id':
                print('\t','LDR r2, =',p[3].val,sep='')
                print('\t','LDR r0, [r2]',sep='')

        #load p[5]
        #if it's a num, we don't need to also load the address
        if p[5].kind == 'num':
                print('\t','LDR r1, =',p[5].val,sep='')
        elif p[5].kind == 'id':
                print('\t','LDR r3, =',p[5].val,sep='')
                print('\t','LDR r1, [r3]',sep='')

        print('\t','LDR r4, =1',sep='')
        print('\t','CMP r0, r1',sep='')
        print('\t','BGT ',label,sep='')
        print('\t','LDR r4, =0',sep='')
        print(label)
        print('\t','LDR r5, =',p[1],sep='')
        print('\t','STR r4, [r2]',sep='')

def p_three_address_instruction_lessequalto(p):
        '''
        three_address_instruction : lhs ASSIGN operand LESSEQUALTO operand
        '''
        #r2: address of operand p[3]
        #r0: value of operand p[3], later the value returned
        #r3: address of operand p[5]
        #r1: value of operand p[5]
        #r4: address of lhs p[1]

        print('\n\t;',p[1],'=',p[3].val,'<',p[5].val)

        label = labelGenerator.new_label()

        #load p[3]
        #if it's a num, we don't need to also load the address
        if p[3].kind == 'num':
                print('\t','LDR r0, =',p[3].val,sep='')
        elif p[3].kind == 'id':
                print('\t','LDR r2, =',p[3].val,sep='')
                print('\t','LDR r0, [r2]',sep='')

        #load p[5]
        #if it's a num, we don't need to also load the address
        if p[5].kind == 'num':
                print('\t','LDR r1, =',p[5].val,sep='')
        elif p[5].kind == 'id':
                print('\t','LDR r3, =',p[5].val,sep='')
                print('\t','LDR r1, [r3]',sep='')

        print('\t','LDR r4, =1',sep='')
        print('\t','CMP r0, r1',sep='')
        print('\t','BLE ',label,sep='')
        print('\t','LDR r4, =0',sep='')
        print(label)
        print('\t','LDR r5, =',p[1],sep='')
        print('\t','STR r4, [r2]',sep='')

def p_three_address_instruction_greaterequalto(p):
        '''
        three_address_instruction : lhs ASSIGN operand GREATEREQUALTO operand
        '''
        #r2: address of operand p[3]
        #r0: value of operand p[3], later the value returned
        #r3: address of operand p[5]
        #r1: value of operand p[5]
        #r4: address of lhs p[1]

        print('\n\t;',p[1],'=',p[3].val,'<',p[5].val)

        label = labelGenerator.new_label()

        #load p[3]
        #if it's a num, we don't need to also load the address
        if p[3].kind == 'num':
                print('\t','LDR r0, =',p[3].val,sep='')
        elif p[3].kind == 'id':
                print('\t','LDR r2, =',p[3].val,sep='')
                print('\t','LDR r0, [r2]',sep='')

        #load p[5]
        #if it's a num, we don't need to also load the address
        if p[5].kind == 'num':
                print('\t','LDR r1, =',p[5].val,sep='')
        elif p[5].kind == 'id':
                print('\t','LDR r3, =',p[5].val,sep='')
                print('\t','LDR r1, [r3]',sep='')

        print('\t','LDR r4, =1',sep='')
        print('\t','CMP r0, r1',sep='')
        print('\t','BGE ',label,sep='')
        print('\t','LDR r4, =0',sep='')
        print(label)
        print('\t','LDR r5, =',p[1],sep='')
        print('\t','STR r4, [r2]',sep='')

def p_three_address_instruction_equalto(p):
        '''
        three_address_instruction : lhs ASSIGN operand EQUALTO operand
        '''
        #r2: address of operand p[3]
        #r0: value of operand p[3], later the value returned
        #r3: address of operand p[5]
        #r1: value of operand p[5]
        #r4: address of lhs p[1]

        print('\n\t;',p[1],'=',p[3].val,'<',p[5].val)

        label = labelGenerator.new_label()

        #load p[3]
        #if it's a num, we don't need to also load the address
        if p[3].kind == 'num':
                print('\t','LDR r0, =',p[3].val,sep='')
        elif p[3].kind == 'id':
                print('\t','LDR r2, =',p[3].val,sep='')
                print('\t','LDR r0, [r2]',sep='')

        #load p[5]
        #if it's a num, we don't need to also load the address
        if p[5].kind == 'num':
                print('\t','LDR r1, =',p[5].val,sep='')
        elif p[5].kind == 'id':
                print('\t','LDR r3, =',p[5].val,sep='')
                print('\t','LDR r1, [r3]',sep='')

        print('result','\t','DCD -1',sep='')
        print('\t','LDR r4, =1',sep='')
        print('\t','CMP r0, r1',sep='')
        print('\t','BEQ ',label,sep='')
        print('\t','LDR r4, =0',sep='')
        print(label)
        print('\t','LDR r5, =',p[1],sep='')
        print('\t','STR r4, [r2]',sep='')

def p_three_address_instruction_notequalto(p):
        '''
        three_address_instruction : lhs ASSIGN operand NOTEQUALTO operand
        '''
        #r2: address of operand p[3]
        #r0: value of operand p[3], later the value returned
        #r3: address of operand p[5]
        #r1: value of operand p[5]
        #r4: address of lhs p[1]

        print('\n\t;',p[1],'=',p[3].val,'<',p[5].val)

        label = labelGenerator.new_label()

        #load p[3]
        #if it's a num, we don't need to also load the address
        if p[3].kind == 'num':
                print('\t','LDR r0, =',p[3].val,sep='')
        elif p[3].kind == 'id':
                print('\t','LDR r2, =',p[3].val,sep='')
                print('\t','LDR r0, [r2]',sep='')

        #load p[5]
        #if it's a num, we don't need to also load the address
        if p[5].kind == 'num':
                print('\t','LDR r1, =',p[5].val,sep='')
        elif p[5].kind == 'id':
                print('\t','LDR r3, =',p[5].val,sep='')
                print('\t','LDR r1, [r3]',sep='')

        print('\t','LDR r4, =1',sep='')
        print('\t','CMP r0, r1',sep='')
        print('\t','BNE ',label ,sep='')
        print('\t','LDR r4, =0',sep='')
        print(label)
        print('\t','LDR r5, =',p[1],sep='')
        print('\t','STR r4, [r2]',sep='')

def p_three_address_instruction_and(p):
        '''
        three_address_instruction : lhs ASSIGN operand AND operand
        '''
        label = labelGenerator.new_label()

        print('\n\t;',p[1],'=',p[3].val,'&&',p[5].val)

        if p[3].kind == 'num':
                print('\t','LDR r0, =',p[3].val,sep='')
        elif p[3].kind == 'id':
                print('\t','LDR r2, =',p[3].val,sep='')
                print('\t','LDR r0, [r2]',sep='')

        #load p[3]
        #if it's a num, we don't need to also load the address
        if p[5].kind == 'num':
                print('\t','LDR r1, =',p[5].val,sep='')
        elif p[5].kind == 'id':
                print('\t','LDR r3, =',p[5].val,sep='')
                print('\t','LDR r1, [r3]',sep='')

        print('\t','LDR r4, =0',sep='')
        print('\t','CMP r0, #0',sep='')
        print('\t','BEQ ',label,sep='')
        print('\t','CMP r1, #0',sep='')
        print('\t','BEQ ',label,sep='')
        print('\t','LDR r4, =1',sep='')
        print(label)
        print('\t','LDR r0, =',p[1],sep='')
        print('\t','STR r4, [r0]',sep='')

def p_three_address_instruction_or(p):
        '''
        three_address_instruction : lhs ASSIGN operand OR operand
        '''
        label = labelGenerator.new_label()

        print('\n\t;',p[1],'=',p[3].val,'||',p[5].val)

        if p[3].kind == 'num':
                print('\t','LDR r0, =',p[3].val,sep='')
        elif p[3].kind == 'id':
                print('\t','LDR r2, =',p[3].val,sep='')
                print('\t','LDR r0, [r2]',sep='')

        #load p[3]
        #if it's a num, we don't need to also load the address
        if p[5].kind == 'num':
                print('\t','LDR r1, =',p[5].val,sep='')
        elif p[5].kind == 'id':
                print('\t','LDR r3, =',p[5].val,sep='')
                print('\t','LDR r1, [r3]',sep='')

        print('\t','LDR r4, =1',sep='')
        print('\t','CMP r0, #0',sep='')
        print('\t','BEQ ',label,sep='')
        print('\t','CMP r1, #0',sep='')
        print('\t','BEQ ',label,sep='')
        print('\t','LDR r4, =0',sep='')
        print(label)
        print('\t','LDR r0, =',p[1],sep='')
        print('\t','STR r4, [r0]',sep='')

def p_three_address_instruction_iffalsegoto(p):
        '''
        three_address_instruction : IFFALSE operand GOTO ID
        '''
        print('\n\t; IFFALSE',p[2].val,'GOTO',p[4])
        if p[2].kind == 'num':
                print('\t','LDR r1, =',p[2].val,sep='')
        elif p[2].kind == 'id':
                print('\t','LDR r3, =',p[2].val,sep='')
                print('\t','LDR r1, [r3]',sep='')

        print('\t','CMP r1, #0',sep='')
        print('\t','BEQ ',p[4],sep='')

def p_three_address_instruction_iftruegoto(p):
        '''
        three_address_instruction : IFTRUE operand GOTO ID
        '''
        print('\n\t; IFTRUE',p[2].val,'GOTO',p[4])
        if p[2].kind == 'num':
                print('\t','LDR r1, =',p[2].val,sep='')
        elif p[2].kind == 'id':
                print('\t','LDR r3, =',p[2].val,sep='')
                print('\t','LDR r1, [r3]',sep='')

        print('\t','CMP r1, #0',sep='')
        print('\t','BNE ',p[4],sep='')

def p_three_address_instruction_goto(p):
        '''
        three_address_instruction : GOTO ID
        '''
        print('\n\t; goto',p[2])
        print('\t','B ',p[2],sep='')

def p_three_address_instruction_write(p):
        '''
        three_address_instruction : WRITE operand
        '''
        #r11: address where we put output
        #   we will increase r11 by 4 so it points to the
        #   next spot for output
        #r0: value to output
        #r1: address of operand p[2]
        #r10: 4 - the amount to increase r11 by

        #printing out a comment with a three-address code
        #version of what we're working on
        print('\n\t; write',p[2].val)

        #load p[2]
        #if it's a num, we don't need to also load the address
        if p[2].kind == 'num':
                print('\t','LDR r0, =',p[2].val,sep='')
        elif p[2].kind == 'id':
                print('\t','LDR r1, =',p[2].val,sep='')
                print('\t','LDR r0, [r1]',sep='')
        
        #store value to output memory location
        print('\t','STR r0, [r11]',sep='')        

        #change r11 to point at the next input value
        print('\t','LDR r10, =4',sep='')      
        print('\t','ADD r11, r11, r10',sep='')

def p_three_address_instruction_read(p):
        '''
        three_address_instruction : READ lhs
        '''

        #r12: address where we find input
        #   we will increase r12 by 4 so it points to the
        #   next value of input
        #r0: value of the input
        #r1: address of lhs p[2]
        #r10: 4 - the amount to increase r12 by

        #printing out a comment with a three-address code
        #version of what we're working on
        print('\n\t; read',p[2])

        #load value at memory location of next input
        print('\t','LDR r0,[r12]',sep='')

        #load memory location of lhs
        print('\t','LDR r1, =',p[2],sep='')

        #store input value to memory location of lhs
        print('\t','STR r0, [r1]',sep='')

        #change r12 to point at the next input value
        print('\t','LDR r10, =4',sep='')      
        print('\t','ADD r12, r12, r10',sep='')


def p_label_list_label(p):
        '''
        label_list : label_list label
        '''
        pass

def p_label_list_empty(p):
        '''
        label_list :
        '''
        pass

def p_lhs(p):
        '''
        lhs : ID
        '''
        #labels in ARM code can't be a single character,
        #so to be on the safe side, we will prefix each
        #variable name with var_
        p[0] = 'var_'+p[1]

        #include this in the set of variables we need to
        #make space in memory for
        variable_set.add(p[0])

def p_operand_id(p):
        '''
        operand : ID
        '''
        #labels in ARM code can't be a single character,
        #so to be on the safe side, we will prefix each
        #variable name with var_
        p[0] = OperandInfo()
        p[0].val = 'var_'+p[1]
        p[0].kind = 'id'

        #include this in the set of variables we need to
        #make space in memory for
        variable_set.add(p[0].val)


def p_operand_num(p):
        '''
        operand : NUM
        '''
        p[0] = OperandInfo()
        p[0].val = p[1]
        p[0].kind = 'num'


#when we see a label, we just need to print the
#ARM label - same name but no colon
def p_label(p):
        '''
        label : ID COLON
        '''
        print(p[1])

  
# Error rule for syntax errors
def p_error(p):
	print(";Syntax error in input!")

# Build the parser
parser = yacc.yacc()

#r12 will be used to keep track of the first address for input
#r11 will be used to keep track of the first address for output
print('\t; initializing the first addresses for the input and output buffers')
print('\tLDR r12, =_input')
print('\tLDR r11, =_output')

#parse the string from standard in
#stop at the EOF character
parser.parse(sys.stdin.read())

#emit the command to end execution here
print('\tEND')

#every output assembly file will contain some procedures
#for doing multiplication and division
mult_div_file = open(this_directory+'/mult_div.asm','r')
mult_div_file_contents = mult_div_file.read()
print(mult_div_file_contents)

print('\n\t; Below is the memory space for variables needed in this program')
for variable_name in variable_set:
        print(variable_name,'\tDCD\t0')

#initializing space for up to 100 input values
print('\n\t; Below is the memory space for memory-mapped input')
print('_input\tDCD\t'+('0,'*99)+'0')

#initializing space for up to 100 output values
print('\n\t; Below is the memory space for memory-mapped output')
print('_output\tDCD\t'+('0,'*99)+'0')





