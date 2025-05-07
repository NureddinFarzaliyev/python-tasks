mail = input("Enter the mail: ")
print(f"{mail.split('@')[0]} at {mail.split('@')[1].split('.')[0]}")