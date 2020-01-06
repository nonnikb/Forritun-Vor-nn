def decrypt(my_str):
    decrypted = ""
    for x, y in enumerate(my_str):
        if x % 3 == 0:
            decrypted += y
    return decrypted
# DO NOT change any code below this comment
print(decrypt(input("Enter the message you want to decrypt: ")))

