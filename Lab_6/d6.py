import string
sentence = input("Input a sentence: ")

# Here you should add the missing part

letters = sentence.split(".")
unique = []

for sentence in letters:
    for letter in sentence:
        if letter not in unique and letter.isalpha():
            unique.append(letter)



print("Unique letters: {}".format(unique))
