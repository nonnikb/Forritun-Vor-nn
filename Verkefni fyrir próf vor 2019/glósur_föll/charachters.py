def get_longest_word(filename):
    longest_word = None
    with open(filename, "r") as Data:
        for line in Data:
            line_word_list = line.strip().split(" ")
            for word in line_word_list:
                if longest_word == None:
                    longest_word = word
                elif len(word) > len(longest_word):
                    longest_word = word
    return longest_word


def get_shortest_word(filename):
    shortest_word = None
    with open(filename, "r") as Data:
        for line in Data:
            line_word_list = line.strip().split(" ")
            for word in line_word_list:
                if word != "":
                    if shortest_word == None:
                        shortest_word = word
                    elif len(word) < len(shortest_word):
                        shortest_word = word
    return shortest_word


def get_all_numbers(filename):
    numbers_in_file = []
    with open(filename, "r") as Data:
        for line in Data:
            for letter in line:
                if letter.isdigit():
                    numbers_in_file.append(letter)
    return numbers_in_file


def get_all_special(filename):
    special_in_file = []
    with open(filename, "r") as Data:
        for line in Data:
            line = line.strip().replace(" ", "")
            for letter in line:
                if not letter.isdigit() and not letter.isalpha():
                    special_in_file.append(letter)
    return special_in_file


def get_all_uppercase(filename):
    uppercase_in_file = []
    with open(filename, "r") as Data:
        for line in Data:
            for letter in line:
                if letter.isupper():
                    uppercase_in_file.append(letter)
    return uppercase_in_file


def get_number_of_words(filename):
    words_in_file = []
    with open(filename, "r") as Data:
        for line in Data:
            words_in_line = line.strip().split(" ")
            words_in_file += words_in_line
    return len(words_in_file)


def main():
    filename = "words.txt"

    longest = get_longest_word(filename)
    print(f"{filename} longest word is '{longest}'")

    shortest = get_shortest_word(filename)
    print(f"{filename} shortest word is '{shortest}'")

    numbers = len(get_all_numbers(filename))
    print(f"{filename} contains {numbers} numbers numbers")

    special = len(get_all_special(filename))
    print(f"{filename} contains {special} special characters")

    upper = len(get_all_uppercase(filename))
    print(f"{filename} contains {upper} uppercase characters")

    count = get_number_of_words(filename)
    print(f"{filename} contains {count} words")


main()