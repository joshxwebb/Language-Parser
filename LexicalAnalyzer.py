import re
import sys

class Lexer:
	def __init__(self, file_data):
		self.myfile = file_data.read()
		print (self.myfile)
		self.lexeme = ""
		self.token = ""
		self.linenum = 1
		self.token_dict = {'RParen':"\\)",
				'LParen':"\\(",
				'Int_Lit':"[0-9][0-9]*",
				'Comment':"#.*",
				'Rel_Op':"(=|<>|<=|<|>=|>)",
				'Mult_Op':"(\\*|/)",
				'Add_Op':"(\\+|-)",
				'Var':"[A-Za-z][A-Za-z0-9]*",
				'If':"if\\b",
				'Save':"save\\b",
				'Load':"load\\b",
				'While':"while\\b",
				'Start':"start\\b",
				'Prog_Name':"[A-Z][A-Za-z0-9]*",
				'Finish':"finish\\b",
				'Then':"then\\b",
				'Else':"else\\b",
				'Do':"do\\b",
				'Assign_Op':":=",
				'Comma':",",
				'Semi_Colon':";",
				'Prog':"prog\\b",
				'Unknown':".+?\s"}
		self.token_list = ['Prog','Load','Save','Start','While',
				'Finish','Then','Else','Do','If','Prog_Name',
				'Var','Int_Lit','Assign_Op','Rel_Op','Mult_Op',
				'Add_Op','Comma','Semi_Colon','RParen',
				'LParen','Comment','Unknown']

	#ignore the blank spaces between tokens
	def ignore_spaces(self):
		ignore = re.match("(\s)+", self.myfile)
		if ignore:
			whitespace = ignore.group()
			for c in whitespace:
				if c == '\n':
					self.linenum += 1
			self.myfile = self.myfile[ignore.end():]

	#ignore the entire line if encounter a comment
	def ignore_comments(self):
		ignore = re.match("#.*", self.myfile)
		if ignore:
			self.myfile = self.myfile[ignore.end():]
			self.ignore_spaces()
	
	#match and return the next token
	def lex(self):
		self.ignore_spaces()
		self.ignore_comments()
		if self.myfile == "":
			self.token = 'EOF'
			self.lexeme = 'EOF'
			return self.token
		for t in self.token_list:
			m = re.match(self.token_dict[t], self.myfile)
			if m:
				#print out the token to follow the trail of the parser
				#print("token:", t)
				self.token = t
				self.lexeme = m.group()
				self.myfile = self.myfile[m.end():]
				return self.token
			
		


			
		
	
