import re

with open("Text.txt", "r") as file:
    data = file.read()



emails = re.findall("[^ ]*@[^ ]*.com",data)
print(emails)

numbers = re.findall("[ (][0-9]{3}[^a-zA-Z]*[0-9]{3}[^a-zA-Z]*[0-9]{4}[ .]",data)
print(numbers)