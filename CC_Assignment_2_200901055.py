import re
import ast

def LexicalAnalysiss(input):
    isOperator = ['+', '-', '/', '^', '|', '=', '*']
    isPunctuator = ['(', ')', '{', '}', '[', ']', ';', ':', "'", '"']
    isSpeial = ['!', '@', '#', '$', '%', '&', '_', '?', '<', '>']
    letters = []
    numbers = []
    operators = []
    punctuators = []
    specialCharacters = []
    datatype = []
    tokens = re.findall(r"\d|\D", input)
    print(tokens)
    for i in range(len(tokens)):
        if tokens[i].isalpha() == True:
            letters.append(tokens[i])
        elif tokens[i].isnumeric() == True:
            numbers.append(tokens[i])
        elif tokens[i] in isOperator:
            operators.append(tokens[i])
        elif tokens[i] in isPunctuator:
            punctuators.append(tokens[i])
        elif tokens[i] in isSpeial:
            specialCharacters.append(tokens[i])
    for i in range(len(tokens)):
        if tokens[i] in letters:
            datatype.append('Alphaphet')
        elif tokens[i] in numbers:
            datatype.append('Number')
        elif tokens[i] in operators:
            datatype.append('Operator')
        elif tokens[i] in punctuators:
            datatype.append('Punctuator')
        elif tokens[i] in specialCharacters:
            datatype.append('Special Character')
    print("Total Number of Tokens: ", len(tokens))
    print("")
    print("Alphabets: ", letters)
    print("Numbers: ", numbers)
    print("Operators: ", operators)
    print("Punctuators: ", punctuators)
    print("Special Characters: ", specialCharacters)
    print("")
    print("     Token          Token Type     ")
    for i in range(len(tokens)):
        print("     "+tokens[i]+"          "+datatype[i]+"     ")

def SyntaxAnalysis(input):
    parsed_output = ast.parse(input)
    syntaxTree = ast.dump(parsed_output)
    print(syntaxTree)

if __name__ == "__main__":
    expression = str(input("Enter an expression: "))
    print("")
    print("Lexical Analysis")
    LexicalAnalysiss(expression)
    print("")
    print("Syntax Analysis")
    SyntaxAnalysis(expression)
