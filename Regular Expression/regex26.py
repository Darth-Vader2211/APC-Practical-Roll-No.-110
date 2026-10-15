import re

s = input("Enter research paper references: ")

doi = re.findall(r'\b10\.\d{4,9}/[^\s]+', s)
years = re.findall(r'\b(?:19|20)\d{2}\b', s)
emails = re.findall(r'[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}', s)
urls = re.findall(r'https?://[^\s]+', s)

print("DOIs:", doi)
print("Publication years:", years)
print("Email addresses:", emails)
print("URLs:", urls)