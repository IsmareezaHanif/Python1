# Input
number = int(input("Enter a number: "))

# Generate multiplication table
for i in range(1, 11):
    print(str(number) + " x " + str(i) + " = " + str(number * i))
