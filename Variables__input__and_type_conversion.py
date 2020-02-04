#Allows user to input different types
userInt = int(input('Enter integer (0 - 155): \n'))
userFlt = (input('Enter float: \n'))
userCharct = (input('Enter character: \n'))
userStr = (input('Enter string: \n'))
#Prints the user inputs in order
print(userInt, userFlt, userCharct, userStr)
#Prints the user inputs in reverse order
print(userStr, userCharct, userFlt, userInt)
#Prints the users int inpiut and converts to character
print(userInt, 'converted to a character is', end = ' ')
print(chr(userInt))
