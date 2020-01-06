import string
mystr = input("Enter a sentence: ")
upper = []
lower = []
digit = []
punct = []

for char in mystr:
    if char.isupper():
        upper.append(char)
    elif char.islower():
        lower.append(char)
    elif char.isdigit():
        digit.append(char)
    elif char in string.punctuation:
        punct.append(char)



print("{:>15}{:>5}".format("Upper case", len(upper)))
print("{:>15} {:>5}".format("Lower case", len(lower)))
print("{:>15}{:>5}".format("Digits", len(digit)))
print("{:>15} {:>5}".format("Punctuation", len(punct)))