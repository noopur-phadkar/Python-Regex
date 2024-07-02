import re

text = "Hello World"

# Case insensitive matching
pattern = re.compile(r"hello", re.IGNORECASE)
match = re.search(pattern, text)
if match:
    print(f"Case Insensitive Matched: {match.group()}")

# Multiline matching
multiline_text = """Hello World
hello universe"""
pattern = re.compile(r"^hello", re.IGNORECASE | re.MULTILINE)
matches = pattern.findall(multiline_text)
print(f"Multiline Matched: {matches}")