string = input("Enter a Word : ")

char = input("Enter a Character : ")

i = 0

count = 0

while (i < len(string)):

    if(string[i] == char):
        count = count + 1

    i = i + 1

print("\n Count of", char, "in", string, "is : ", count)

print("\n")

