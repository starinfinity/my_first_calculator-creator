import os

f = open("calculator_github.txt", "x")
f.write("# my_first_calculator.py by AceLewis")
f.write("# support for 100 by Rahul Gahlot(github.com/starinfinity)")
f.write("# TODO: Make it work for all floating point numbers too")
f.write("if 3/2 == 1:  # Because Python 2 does not know maths")
f.write("\tinput = raw_input  # Python 2 compatibility")

f.write("print('Welcome to this calculator!')")
f.write("print('It can add, subtract, multiply and divide whole numbers from 0 to 50')")
f.write("num1 = int(input('Please choose your first number: '))")
f.write("sign = input('What do you want to do? +, -, /, or *: ')")
f.write("num2 = int(input('Please choose your second number: '))")

i = 0
while i < 1000:
    j = 0
    while j < 1000:
        f.write("if num1 == %d and sign == '+' and num2 == %d :" %(i , j))
        f.write("\tprint(\" %d + %d = %d \"" %(i, j, i+j))
        j += 1
    i += 1

i = 0
while i < 1000:
    j = 0
    while j < 1000:
        f.write("if num1 == %d and sign == '-' and num2 == %d :" %(i , j))
        f.write("\tprint(\" %d - %d = %d \"" %(i, j, i-j))
        j += 1
    i += 1

i = 0
while i < 1000:
    j = 0
    while j < 1000:
        f.write("if num1 == %d and sign == '*' and num2 == %d :" %(i , j))
        f.write("\tprint(\" %d + %d = %d \"" %(i, j, i*j))
        j += 1
    i += 1


i = 1
while i < 1000:
    j = 0
    while j < 1000:
        if i == 0 or j == 0:
            f.write("if num1 == %d and sign == '/' and num2 == %d :" %(i , j))
            f.write("\tprint(\" %d + %d = 0 \"" %(i, j))
            j += 1
        else:
            f.write("if num1 == %d and sign == '/' and num2 == %d :" %(i , j))
            f.write("\tprint(\" %d + %d = %d \"" %(i, j, i/j))
            j += 1
    i += 1

f.write("print(\"Thanks for using this calculator, goodbye :)\")")

f.close()

os.rename("calculator_github.txt", "my_first_calculator.py")
