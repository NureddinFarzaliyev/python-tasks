import re
file = open('fradulent_emails.txt', 'r', encoding='utf-8', errors='ignore')
for line in file:
    if re.match('^Message-Id:', line):
        print(line.split(" ")[1][1:-2])
