def sum(x,y):
   return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def devide(x,y):
    return x/y

def mod(x,y):
    return x%y

print(
    """
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Modulus
    """)

choice = int(input("Enter choice (1/2/3/4/5): "))
number1 = int(input("number 1 "))
number2 = int(input("number 2 "))

if(choice == 1):
    print(sum(number1,number2))

if(choice == 2):
    print(sub(number1,number2))

if(choice == 3):
    print(mul(number1,number2))

if(choice == 4):
    print(devide(number1,number2))


if(choice == 5):
    print(mod(number1,number2))


