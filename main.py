# This is a simple calculator which will calculate addition, subtraction, multiplication & division of 2 numbers.

# Step 1 : Create functions for addition, subtraction, multiplication, division.
# Step 2 : Greet User and inform about calculator and the operations possible.
# Step 3 : Ask user for inputting both numbers and store them in variables.
# Step 4 : Give choices using print, and ask user for operation.
# Step 5 : If elif code to check choice made and inside that function to be applied along with the print statement.
# Step 6 : Thank user for using calculator and ask to restart program.

def addi(a, b):
    return a + b


def subs(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    return a / b


print("Hey there! This is a simple calculator.")
print("You can do the following operations on 2 numbers using this :")
print("Addition, Subtraction, Multiplication & Division")

x = float(input("Please enter first number:"))
y = float(input("Please enter second number:"))
z = int(input("Type 1 for Addition, 2 for subtraction, 3 for multiplication & 4 for division: "))

if z == 1:
    print("The result is ", addi(x, y))
elif z == 2:
    print("The result is ", subs(x, y))
elif z == 3:
    print("The result is :", mult(x, y))
elif z == 4:
    print("The result is ", div(x, y))
else:
    print("Please restart the program and choose the correct option.")
