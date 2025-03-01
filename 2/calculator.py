a = input("Enter a Operator : ")

if a == 'Addition':
    b = int(input("Enter a number : "))
    c = int(input("Enter a number : "))
    d = b + c
    print(d)

elif a == 'Subtraction':
    b = int(input("Enter a number : "))
    c = int(input("Enter a number : "))
    d = b - c
    print(d)

elif a == 'Multiplication':
    b = int(input("Enter a number : "))
    c = int(input("Enter a number : "))
    d = b * c
    print(d)

elif a == 'Division':
    b = int(input("Enter a number : "))
    c = int(input("Enter a number : "))
    d = b / c
    print(d)

else:
    print("Invalid Operator")
    
