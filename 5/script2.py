rows = int(input("Enter the number of rows : "))

numbers = 1

print("Floyd's Triangle")

for i in range(1, rows+1):
    for j in range(1, i+1):
        print(numbers, end=" ")
        numbers += 1
    print()