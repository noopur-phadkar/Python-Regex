import re

# Example: Matching a pattern at the start of a string
pattern = r"hello"
text = "hello world"
match = re.match(pattern, text)

if match:
    print(f"Matched: {match.group()}")
else:
    print("No match found")
