print("""
Operation to perfom
\t 1.Addition 
\t 2.Subtraction
\t 3.Multiplication
\t 4.division 
""")

operator = int(input("pick operation from Menu: "))
x = int(input("Enter first number: "))
y = int(input("Enter secon number: "))

if operator ==1:
    answer = x+y 
    if answer%2 ==0:
        print("your answer is an even number ")
    else:
        print("your answer is an odd number")
elif operator == 2:
    answer = x-y 
    if answer%2 ==0:
        print("your answer is an even number ")
    else:
        print("your answer is an odd number")
elif operator == 3:
    answer = x*y 
    if answer%2 ==0:
        print("your answer is an even number ")
    else:
        print("your answer is an odd number")
elif operator == 4:
    answer = x/y 
    if answer%2 ==0:
        print("your answer is an even number ")
    else:
        print("your answer is an odd number")
else:
    print("please select operation from Menu")
