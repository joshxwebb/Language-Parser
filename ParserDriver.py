from SyntaxAnalyzer import Syntax_Analyzer
import sys

myfile = open(sys.argv[1], "r")

if myfile.mode == "r":
    Parser = Syntax_Analyzer(myfile)
else:
    print("Error reading from file")

   