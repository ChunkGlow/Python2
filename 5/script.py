print("Half Pyramid Pattern of Stars (*) : ")

n = int(input("Enter the number of rows : "))

for i in range(n, 1, -1):
    for j in range(i+1):
        print("*", end="")
    print()

for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()
