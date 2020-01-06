def get_emails():
    emails = []
    while True:
        email = input("Email address: ")
        if email != "q":
            emails.append(email)
        else:
            break
    return emails



def get_names_and_domains(email):
    listi = []
    for x in email:
        split = x.split("@")
        listi.append(tuple(split))
    return listi


# DO NOT change any code below this comment
email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)