import re

with open("Text.txt", "r") as file:
    data = file.read()

emails = re.findall("[^ ]*@.*.com",data)
print(emails)