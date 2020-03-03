
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN DIVIDE ELSE EQUALTO GREATEREQUALTO GREATERTHAN ID IF INT LBRACE LESSEQUALTO LESSTHAN LPAREN MINUS MODULO NOT NOTEQUALTO NUM OR PLUS RBRACE READ RPAREN SEMICOLON TIMES WHILE WRITE\n\tprogram : block\n\t\n\tblock : LBRACE action_new_scope stmt_list RBRACE\n\t\n\taction_new_scope : \n\t\n\tstmt_list : stmt_list stmt\n\t\n\tstmt_list : \n\t\n\tstmt : type ID SEMICOLON\n\t\n    stmt : ID ASSIGN expr SEMICOLON\n\t\n\tstmt : block\n\t\n\tstmt : READ ID SEMICOLON\n\t\n\tstmt : WRITE logicor SEMICOLON\n\t\n\tstmt : IF LPAREN logicor RPAREN block\n\t\n\tstmt : IF LPAREN logicor RPAREN block ELSE block\n\t\n\tstmt : WHILE LPAREN logicor RPAREN block\n\t\n\ttype : INT\n\t\n\tlogicor : logicor OR logicand\n\t\n\tlogicor : logicand\n\t\n\tlogicand : logicand AND compEq\n\t\n\tlogicand : compEq\n\t\n\tcompEq : compEq EQUALTO comp\n\t\n\tcompEq : compEq NOTEQUALTO comp\n\t\n\tcompEq : comp\n\t\n\tcomp : comp LESSTHAN expr\n\t\n\tcomp : comp LESSEQUALTO expr\n\t\n\tcomp : comp GREATERTHAN expr\n\t\n\tcomp : comp GREATEREQUALTO expr\n\t\n\tcomp : expr\n\t\n\texpr : expr PLUS term\n\t\n\texpr : expr MINUS term\n\t\n\texpr : term\n\t\n\tterm : term TIMES factor\n\t\n\tterm : term DIVIDE factor\n\t\n\tterm : term MODULO factor\n\t\n\tterm : factor\n\t\n\tfactor : MINUS factor\n\t\n\tfactor : NOT factor\n\t\n\tfactor : ID\n\t\n\tfactor : NUM\n\t\n\tfactor : LPAREN logicor RPAREN\n\t'
    
_lr_action_items = {'LBRACE':([0,3,4,5,6,7,10,33,35,36,55,70,71,72,73,74,75,],[3,-3,-5,3,-2,-4,-8,-6,-9,-10,-7,3,3,-11,-13,3,-12,]),'$end':([1,2,6,],[0,-1,-2,]),'RBRACE':([3,4,5,6,7,10,33,35,36,55,72,73,75,],[-3,-5,6,-2,-4,-8,-6,-9,-10,-7,-11,-13,-12,]),'ID':([3,4,5,6,7,8,10,11,12,15,17,25,27,30,31,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,55,72,73,75,],[-3,-5,9,-2,-4,16,-8,18,28,-14,28,28,28,28,28,28,-6,-9,-10,28,28,28,28,28,28,28,28,28,28,28,28,28,-7,-11,-13,-12,]),'READ':([3,4,5,6,7,10,33,35,36,55,72,73,75,],[-3,-5,11,-2,-4,-8,-6,-9,-10,-7,-11,-13,-12,]),'WRITE':([3,4,5,6,7,10,33,35,36,55,72,73,75,],[-3,-5,12,-2,-4,-8,-6,-9,-10,-7,-11,-13,-12,]),'IF':([3,4,5,6,7,10,33,35,36,55,72,73,75,],[-3,-5,13,-2,-4,-8,-6,-9,-10,-7,-11,-13,-12,]),'WHILE':([3,4,5,6,7,10,33,35,36,55,72,73,75,],[-3,-5,14,-2,-4,-8,-6,-9,-10,-7,-11,-13,-12,]),'INT':([3,4,5,6,7,10,33,35,36,55,72,73,75,],[-3,-5,15,-2,-4,-8,-6,-9,-10,-7,-11,-13,-12,]),'ELSE':([6,72,],[-2,74,]),'ASSIGN':([9,],[17,]),'MINUS':([12,17,23,24,25,26,27,28,29,30,31,32,34,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,60,61,62,63,64,65,66,67,68,69,],[25,25,46,-29,25,-33,25,-36,-37,25,25,25,46,25,25,25,25,25,25,25,25,25,25,25,25,25,-34,-35,46,46,46,46,-27,-28,-30,-31,-32,-38,]),'NOT':([12,17,25,27,30,31,32,37,38,39,40,41,42,43,44,45,46,47,48,49,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'NUM':([12,17,25,27,30,31,32,37,38,39,40,41,42,43,44,45,46,47,48,49,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'LPAREN':([12,13,14,17,25,27,30,31,32,37,38,39,40,41,42,43,44,45,46,47,48,49,],[30,31,32,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'SEMICOLON':([16,18,19,20,21,22,23,24,26,28,29,34,50,51,56,57,58,59,60,61,62,63,64,65,66,67,68,69,],[33,35,36,-16,-18,-21,-26,-29,-33,-36,-37,55,-34,-35,-15,-17,-19,-20,-22,-23,-24,-25,-27,-28,-30,-31,-32,-38,]),'OR':([19,20,21,22,23,24,26,28,29,50,51,52,53,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,],[37,-16,-18,-21,-26,-29,-33,-36,-37,-34,-35,37,37,37,-15,-17,-19,-20,-22,-23,-24,-25,-27,-28,-30,-31,-32,-38,]),'RPAREN':([20,21,22,23,24,26,28,29,50,51,52,53,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,],[-16,-18,-21,-26,-29,-33,-36,-37,-34,-35,69,70,71,-15,-17,-19,-20,-22,-23,-24,-25,-27,-28,-30,-31,-32,-38,]),'AND':([20,21,22,23,24,26,28,29,50,51,56,57,58,59,60,61,62,63,64,65,66,67,68,69,],[38,-18,-21,-26,-29,-33,-36,-37,-34,-35,38,-17,-19,-20,-22,-23,-24,-25,-27,-28,-30,-31,-32,-38,]),'EQUALTO':([21,22,23,24,26,28,29,50,51,57,58,59,60,61,62,63,64,65,66,67,68,69,],[39,-21,-26,-29,-33,-36,-37,-34,-35,39,-19,-20,-22,-23,-24,-25,-27,-28,-30,-31,-32,-38,]),'NOTEQUALTO':([21,22,23,24,26,28,29,50,51,57,58,59,60,61,62,63,64,65,66,67,68,69,],[40,-21,-26,-29,-33,-36,-37,-34,-35,40,-19,-20,-22,-23,-24,-25,-27,-28,-30,-31,-32,-38,]),'LESSTHAN':([22,23,24,26,28,29,50,51,58,59,60,61,62,63,64,65,66,67,68,69,],[41,-26,-29,-33,-36,-37,-34,-35,41,41,-22,-23,-24,-25,-27,-28,-30,-31,-32,-38,]),'LESSEQUALTO':([22,23,24,26,28,29,50,51,58,59,60,61,62,63,64,65,66,67,68,69,],[42,-26,-29,-33,-36,-37,-34,-35,42,42,-22,-23,-24,-25,-27,-28,-30,-31,-32,-38,]),'GREATERTHAN':([22,23,24,26,28,29,50,51,58,59,60,61,62,63,64,65,66,67,68,69,],[43,-26,-29,-33,-36,-37,-34,-35,43,43,-22,-23,-24,-25,-27,-28,-30,-31,-32,-38,]),'GREATEREQUALTO':([22,23,24,26,28,29,50,51,58,59,60,61,62,63,64,65,66,67,68,69,],[44,-26,-29,-33,-36,-37,-34,-35,44,44,-22,-23,-24,-25,-27,-28,-30,-31,-32,-38,]),'PLUS':([23,24,26,28,29,34,50,51,60,61,62,63,64,65,66,67,68,69,],[45,-29,-33,-36,-37,45,-34,-35,45,45,45,45,-27,-28,-30,-31,-32,-38,]),'TIMES':([24,26,28,29,50,51,64,65,66,67,68,69,],[47,-33,-36,-37,-34,-35,47,47,-30,-31,-32,-38,]),'DIVIDE':([24,26,28,29,50,51,64,65,66,67,68,69,],[48,-33,-36,-37,-34,-35,48,48,-30,-31,-32,-38,]),'MODULO':([24,26,28,29,50,51,64,65,66,67,68,69,],[49,-33,-36,-37,-34,-35,49,49,-30,-31,-32,-38,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'block':([0,5,70,71,74,],[2,10,72,73,75,]),'action_new_scope':([3,],[4,]),'stmt_list':([4,],[5,]),'stmt':([5,],[7,]),'type':([5,],[8,]),'logicor':([12,30,31,32,],[19,52,53,54,]),'logicand':([12,30,31,32,37,],[20,20,20,20,56,]),'compEq':([12,30,31,32,37,38,],[21,21,21,21,21,57,]),'comp':([12,30,31,32,37,38,39,40,],[22,22,22,22,22,22,58,59,]),'expr':([12,17,30,31,32,37,38,39,40,41,42,43,44,],[23,34,23,23,23,23,23,23,23,60,61,62,63,]),'term':([12,17,30,31,32,37,38,39,40,41,42,43,44,45,46,],[24,24,24,24,24,24,24,24,24,24,24,24,24,64,65,]),'factor':([12,17,25,27,30,31,32,37,38,39,40,41,42,43,44,45,46,47,48,49,],[26,26,50,51,26,26,26,26,26,26,26,26,26,26,26,26,26,66,67,68,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> block','program',1,'p_program','parser.py',88),
  ('block -> LBRACE action_new_scope stmt_list RBRACE','block',4,'p_block','parser.py',95),
  ('action_new_scope -> <empty>','action_new_scope',0,'p_action_new_scope','parser.py',102),
  ('stmt_list -> stmt_list stmt','stmt_list',2,'p_stmt_list','parser.py',112),
  ('stmt_list -> <empty>','stmt_list',0,'p_stmt_list_empty','parser.py',120),
  ('stmt -> type ID SEMICOLON','stmt',3,'p_stmt_decl','parser.py',128),
  ('stmt -> ID ASSIGN expr SEMICOLON','stmt',4,'p_stmt_assign','parser.py',142),
  ('stmt -> block','stmt',1,'p_stmt_block','parser.py',154),
  ('stmt -> READ ID SEMICOLON','stmt',3,'p_stmt_read','parser.py',161),
  ('stmt -> WRITE logicor SEMICOLON','stmt',3,'p_stmt_write','parser.py',172),
  ('stmt -> IF LPAREN logicor RPAREN block','stmt',5,'p_stmt_if','parser.py',178),
  ('stmt -> IF LPAREN logicor RPAREN block ELSE block','stmt',7,'p_stmt_if_else','parser.py',184),
  ('stmt -> WHILE LPAREN logicor RPAREN block','stmt',5,'p_while','parser.py',190),
  ('type -> INT','type',1,'p_type','parser.py',197),
  ('logicor -> logicor OR logicand','logicor',3,'p_logicor_logicor','parser.py',203),
  ('logicor -> logicand','logicor',1,'p_logicor_logicand','parser.py',209),
  ('logicand -> logicand AND compEq','logicand',3,'p_logicand_logicand','parser.py',215),
  ('logicand -> compEq','logicand',1,'p_logicand_compEq','parser.py',221),
  ('compEq -> compEq EQUALTO comp','compEq',3,'p_compEq_equal','parser.py',227),
  ('compEq -> compEq NOTEQUALTO comp','compEq',3,'p_compEq_notequal','parser.py',233),
  ('compEq -> comp','compEq',1,'p_compEq_comp','parser.py',239),
  ('comp -> comp LESSTHAN expr','comp',3,'p_comp_less','parser.py',245),
  ('comp -> comp LESSEQUALTO expr','comp',3,'p_comp_lessequal','parser.py',251),
  ('comp -> comp GREATERTHAN expr','comp',3,'p_comp_greater','parser.py',257),
  ('comp -> comp GREATEREQUALTO expr','comp',3,'p_comp_greaterequal','parser.py',263),
  ('comp -> expr','comp',1,'p_comp_compEq','parser.py',269),
  ('expr -> expr PLUS term','expr',3,'p_expr_plus','parser.py',277),
  ('expr -> expr MINUS term','expr',3,'p_expr_minus','parser.py',283),
  ('expr -> term','expr',1,'p_expr_term','parser.py',289),
  ('term -> term TIMES factor','term',3,'p_term_times','parser.py',297),
  ('term -> term DIVIDE factor','term',3,'p_term_divide','parser.py',303),
  ('term -> term MODULO factor','term',3,'p_term_modulo','parser.py',309),
  ('term -> factor','term',1,'p_term_factor','parser.py',315),
  ('factor -> MINUS factor','factor',2,'p_factor_minus','parser.py',321),
  ('factor -> NOT factor','factor',2,'p_factor_not','parser.py',327),
  ('factor -> ID','factor',1,'p_factor_id','parser.py',335),
  ('factor -> NUM','factor',1,'p_factor_num','parser.py',347),
  ('factor -> LPAREN logicor RPAREN','factor',3,'p_factor_parens','parser.py',354),
]
