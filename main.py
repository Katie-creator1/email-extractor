import re

# Define regex pattern for standard email formats
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+'

# Load sample text file
sample_emails = 'sample_emails.txt'

with open(sample_emails, 'r') as file:
    text = file.read()

# Find all matching email addresses
emails = re.findall(pattern, text)

# Remove duplicates using a set
unique_emails = set(emails)

# Print each unique email
for email in unique_emails:
    print(email)
