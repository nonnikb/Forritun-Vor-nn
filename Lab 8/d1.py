def cdo(setning):
    word_list = setning.split()
    word_list.sort()
    sent = ""
    for word in word_list:
        sent += word + " "
    return sent

print(cdo(input("Enter a string: ")))