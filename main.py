import re

with open("Text.txt", "r") as file:
    data = file.read()

def standardize_numbers(number_input):
    num = list("0123456789")
    formated_number = ""
    for char in number_input:
        if char in num:
            if len(formated_number) == 3 or  len(formated_number) == 7:
                formated_number += "-"
            formated_number += char
    return formated_number

def format_numbers(text_list):
    formated_list = []
    formated_string = ""
    for number in text_list:
        formated_list.append(standardize_numbers(number))
    num = len(formated_list)-1
    for index,number in enumerate(formated_list):
        if index == 0:
            formated_string += number
        elif num == index:
            formated_string += f" or {number}"
        else:
            formated_string += f", {number}"
    return formated_string

def format_email(email_list):
    email_string = ""
    num = len(email_list)-1
    for index, email in enumerate(email_list):
        if index == 0:
            email_string += email
        elif num == index:
            email_string += f" or {email}"
        else:
            email_string += f", {email}"
    return email_string



emails = re.findall("[^ ]*@[^ ]*.com",data)
numbers = re.findall("[ (][0-9]{3}[^a-zA-Z]*[0-9]{3}[^a-zA-Z]*[0-9]{4}[ .]",data)

email_strings = format_email(emails)
numbers_string = format_numbers(numbers)

print(f"Contact information is:\nEmails: {email_strings}\nNumbers: {numbers_string}")