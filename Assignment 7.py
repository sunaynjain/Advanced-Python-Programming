import re

def find_emails(text):
    pattern = r'[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}'
    return re.findall(pattern, text)

text = input("Enter text: ")

emails = find_emails(text)

print("Email addresses:", emails)
