import re

pattern = r"world"
text = "hello world"
match = re.search(pattern, text)

if match:
    print(f"Matched: {match.group()}")
else:
    print("No match found")