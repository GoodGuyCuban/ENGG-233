# calculator.py
# Marcos Perez, ENDG 233 F21
#
# A terminal-based calculator application for determining the result of a mathematical expression containing three values and two operators.
# Detailed specifications are provided via the Assignment 1 handout.
#
print('Enter the first value:') # setting up variables and taking in input
value1 = int(input())
print('Enter the first operator:')
first_operator = str(input())
print('Enter the second value:')
value2 = int(input())
print('Enter the second operator:')
second_operator = str(input())
print('Enter the third value:')
value3 = int(input())

if first_operator == '+': # main logic switch, identifies what the first operator is 
    # (note: all operator switches account for an unexpected input, will terminate the program and give an error if invalid input is detected)
    if second_operator == '+': # minor logic switch, identifies what the second operator is and calculates/prints the expression once the operator is determined. (same for below)
        print('Entered expression:',value1,first_operator,value2,second_operator,value3)
        print('Your final answer =',value1 + value2 + value3)
    elif second_operator == '-':
        print('Entered expression:',value1,first_operator,value2,second_operator,value3)
        print('Your final answer =',value1 + value2 - value3)
    elif second_operator == '*':
        print('Entered expression:',value1,first_operator,value2,second_operator,value3)
        print('Your final answer =',value1 + (value2 * value3))
    elif second_operator == '/':
        print('Entered expression:',value1,first_operator,value2,second_operator,value3)
        print('Your final answer =',value1 + (value2 // value3))
    else:
        print('ERROR:(invalid operator) please enter a valid operator (+,-,*,/)')
        quit
elif first_operator == '-':
    if second_operator == '+': # minor logic switch, identifies what the second operator is
        print('Entered expression:',value1,first_operator,value2,second_operator,value3)
        print('Your final answer =',value1 - value2 + value3)
    elif second_operator == '-':
        print('Entered expression:',value1,first_operator,value2,second_operator,value3)
        print('Your final answer =',value1 - value2 - value3)
    elif second_operator == '*':
        print('Entered expression:',value1,first_operator,value2,second_operator,value3)
        print('Your final answer =',value1 - (value2 * value3))
    elif second_operator == '/':
        print('Entered expression:',value1,first_operator,value2,second_operator,value3)
        print('Your final answer =',value1 - (value2 // value3))
    else:
        print('ERROR:(invalid operator) please enter a valid operator (+,-,*,/)')
        quit
elif first_operator == '*':
    if second_operator == '+': # minor logic switch, identifies what the second operator is
        print('Entered expression:',value1,first_operator,value2,second_operator,value3)
        print('Your final answer =',(value1 * value2) + value3)
    elif second_operator == '-':
        print('Entered expression:',value1,first_operator,value2,second_operator,value3)
        print('Your final answer =',(value1 * value2) - value3)
    elif second_operator == '*':
        print('Entered expression:',value1,first_operator,value2,second_operator,value3)
        print('Your final answer =',(value1 * value2) * value3)
    elif second_operator == '/':
        print('Entered expression:',value1,first_operator,value2,second_operator,value3)
        print('Your final answer =',value1 * (value2 // value3))
    else:
        print('ERROR:(invalid operator) please enter a valid operator (+,-,*,/)')
        quit
elif first_operator == '/':
    if second_operator == '+': # minor logic switch, identifies what the second operator is
        print('Entered expression:',value1,first_operator,value2,second_operator,value3)
        print('Your final answer =',(value1 // value2) + value3)
    elif second_operator == '-':
        print('Entered expression:',value1,first_operator,value2,second_operator,value3)
        print('Your final answer =',(value1 // value2) - value3)
    elif second_operator == '*':
        print('Entered expression:',value1,first_operator,value2,second_operator,value3)
        print('Your final answer =',(value1 // value2) * value3)
    elif second_operator == '/':
        print('Entered expression:',value1,first_operator,value2,second_operator,value3)
        print('Your final answer =',(value1 // value2) // value3)
    else:
        print('ERROR:(invalid operator) please enter a valid operator (+,-,*,/)')
        quit
else:
    print('ERROR:(invalid operator) please enter a valid operator (+,-,*,/)')
    quit

# In hindsight, I have noticed that I can make many improvements to this program, 
# it works perfectly to the specifications, but I definitely could have reduced the amount of if/elif statements.
# Other than the obvious bloat, I quite like this program. As a person used to programming in Java, I think i'm starting to like python, nice and simple :-) 