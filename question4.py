# Input
s = input("Enter a string: ")

# Count vowels
count = sum(1 for c in s if c in "aeiouAEIOU")

# Output
print('The number of vowels in "' + s + '" is ' + str(count) + '.')
