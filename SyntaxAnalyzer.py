from LexicalAnalyzer import Lexer

class Syntax_Analyzer:
	def __init__(self, myfile):
		self.if_error = False
		self.lexer = Lexer(myfile)
		self.lexer.lex()
		self.prog_start()

	#<program> ::= prog <progname> <compound stmt>
	def prog_start(self):
		if self.lexer.token == 'Prog':
			self.lexer.lex()
		else:
			self.error('Prog')
		if self.lexer.token == 'Prog_Name':
			self.lexer.lex()	
		else:
			self.error('Prog_Name')
		self.compound_stmt()
		while self.lexer.token != 'EOF':
			self.error('EOF')
			self.lexer.lex()
		if not self.if_error:
			print("Code parsed successfully")

	#<compound stmt> ::= start <stmt> {; <stmt>} finish
	def compound_stmt(self):
		if self.lexer.token == 'Start':
			self.lexer.lex()
		else:
			self.error('Start')
		self.stmt()
		while self.lexer.token == 'Semi_Colon':
			self.lexer.lex()
			self.stmt()
		if self.lexer.token == 'Finish':
			self.lexer.lex()
		else:
			self.error('Finish')
	
	#<stmt> ::= <simple stmt> | <structured stmt>
	def stmt(self):
		if self.lexer.token in ('Load', 'Save', 'Var', 'Prog_Name'):
			self.simple_stmt()
		elif self.lexer.token in ('If', 'While', 'Start'):
			self.structured_stmt()
		else:
			self.error('Load, Save, Var, If, While, or Start')
			self.lexer.lex()

	#<simple stmt> ::= <assignment stmt> | <load stmt> | <save stmt>
	def simple_stmt(self):
		if self.lexer.token == 'Load':
			self.load_stmt()
		elif self.lexer.token == 'Save':
			self.save_stmt()
		elif self.lexer.token in ('Var', 'Prog_Name'):
			self.assignment_stmt()
		else:
			#should only come into this method with one of the above tokens
			#so this error should never occur
			self.error('Load, Save, or Var')
	
	#<structured stmt> ::= <compound stmt> | <if stmt> | <while stmt>
	def structured_stmt(self):
		if self.lexer.token == 'If':
			self.if_stmt()
		elif self.lexer.token == 'While':
			self.while_stmt()
		elif self.lexer.token == 'Start':
			self.compound_stmt()
		else:
			#should only come into this method with one of the above tokens
			#so this error should never occur
			self.error('If, While, or Start')

	#<load stmt> ::= load ( <variable> { , <variable> } )
	def load_stmt(self):
		if self.lexer.token == 'Load':
			self.lexer.lex()
		else:
			self.error('Load')
		if self.lexer.token == 'LParen':
			self.lexer.lex()
		else:
			self.error('LParen')
		if self.lexer.token in ('Var', 'Prog_Name'):
			self.lexer.lex()
		else:
			self.error('Var')
		while self.lexer.token == 'Comma':
			self.lexer.lex()
			if self.lexer.token in ('Var', 'Prog_Name'):
				self.lexer.lex()
			else:
				self.error('Var')

		if self.lexer.token == 'RParen':
			self.lexer.lex()
		else:
			self.error('RParen')

	#<save stmt> ::= save ( <expression> { , <expression> } )
	def save_stmt(self):
		if self.lexer.token == 'Save':
			self.lexer.lex()
		else:
			self.error('Save')
		if self.lexer.token == 'LParen':
			self.lexer.lex()		
		else:
			self.error('LParen')
		self.expression()
		while self.lexer.token == 'Comma':
			self.lexer.lex()
			self.expression()
		if self.lexer.token == 'RParen':
			self.lexer.lex()
		else:
			self.error('RParen')
		
	#<assignment stmt> ::= <variable> := <expression>
	def assignment_stmt(self):
		if self.lexer.token in ('Var', 'Prog_Name'):
			self.lexer.lex()
		else:
			self.error('Var')
		if self.lexer.token == 'Assign_Op':
			self.lexer.lex()	
		else:
			self.error('Assign_Op')
		self.expression()		

	#<if stmt> ::= if <expression> then <stmt> | if <expression> then <stmt> else <stmt>
	def if_stmt(self):
		if self.lexer.token == 'If':
			self.lexer.lex()
		else:
			self.error('If')
		self.expression()	
		if self.lexer.token == 'Then':
			self.lexer.lex()
		else:
			self.error('Then')
		self.stmt()
		if self.lexer.token == 'Else':
			self.lexer.lex()
			self.stmt()
	
	#<while stmt> ::= while <expression> do <stmt>
	def while_stmt(self):
		if self.lexer.token == 'While':
			self.lexer.lex()
		else :
			self.error('While')
		self.expression()
		if self.lexer.token == 'Do':
			self.lexer.lex()	
		else:
			self.error('Do')
		self.stmt()
		
	#<expression> ::= <simple expr> | <simple expr> <relational_operator> <simple expr>			
	def expression(self):
		self.simple_expression()
		if self.lexer.token == 'Rel_Op':
			self.lexer.lex()
			self.simple_expression()

	#<simple expr> ::= [ <sign> ] <term> { <adding_operator> <term> }
	def simple_expression(self):
		if self.lexer.token == 'Add_Op':
			self.lexer.lex()
		self.term()
		while self.lexer.token == 'Add_Op':
			self.lexer.lex()
			self.term()

	#<term> ::= <factor> { <multiplying_operator> <factor> }
	def term(self):
		self.factor()
		while self.lexer.token == 'Mult_Op':
			self.lexer.lex()
			self.factor()
	
	#<factor> ::= <variable> | <int_literal> | ( <expression> )
	def factor(self):
		if self.lexer.token == 'LParen':
			self.lexer.lex()
			self.expression()
			if self.lexer.token == 'RParen':
				self.lexer.lex()
		elif self.lexer.token in ('Var', 'Prog_Name', 'Int_Lit'):
			self.lexer.lex()
		else:
			self.error('LParen, Var, or Int_Lit')

	#report syntax error
	def error(self, expected_token):
		print ("SYNTAX ERROR: found ", self.lexer.token, "on line ", 
		self.lexer.linenum, " but expected ", expected_token)
		self.if_error = True
		

