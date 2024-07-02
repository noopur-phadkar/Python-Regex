import re

pattern = r"\((?:[^()]+|(?R))*\)"
text = "a(b(c)d)e"
match = re.search(pattern, text)
if match:
    print(f"Matched: {match.group()}")  # Output: "(b(c)d)"