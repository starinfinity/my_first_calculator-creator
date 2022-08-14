import os

f = open("calculator_github.py", "w")
f.write("# my_first_calculator.py by AceLewis\n")
f.write("# support for 100 by Rahul Gahlot(github.com/starinfinity)\n")
f.write("# TODO: Make it work for all floating point numbers too\n")
f.write("if 3/2 == 1:  # Because Python 2 does not know maths\n")
f.write("\tinput = raw_input  # Python 2 compatibility\n")

f.write("print('Welcome to this calculator!')\n")
f.write("print('It can add, subtract, multiply and divide whole numbers from 0 to 50')\n")
f.write("num1 = int(input('Please choose your first number: '))\n")
f.write("sign = input('What do you want to do? +, -, /, or *: ')\n")
f.write("num2 = int(input('Please choose your second number: '))\n")
f.write("cal_dict = {\n")
i = 0
while i < 50:
    j = 0
    while j < 50:
        f.write(f"\t\"{i}+{j}\": \"{i+j}\",\n")
        j += 1
    i += 1
i = 0
while i < 50:
    j = 0
    while j < 50:
        f.write(f"\t\"{i}-{j}\": \"{i-j}\",\n")
        j += 1
    i += 1
i = 0
while i < 50:
    j = 0
    while j < 50:
        f.write(f"\t\"{i}*{j}\": \"{i*j}\",\n")
        j += 1
    i += 1
i = 0
while i < 50:
    j = 0
    while j < 50:
        try:
            f.write(f"\t\"{i}/{j}\": \"{i/j}\",\n")
        except ZeroDivisionError:
            f.write(f"\t\"{i}/{j}\": \"Inf\",\n")
        j += 1
    i += 1


f.write("}\n")
f.write("print(cal_dict[f\"{num1}{sign}{num2}\"])\n")
