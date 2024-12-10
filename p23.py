import re
# Search for a pattern
text = "My phone number is 123-456-7890."
pattern = r"\d{3}-\d{3}-\d{4}"
match = re.search(pattern, text)
print(match.group()) # Output: 123-456-7890