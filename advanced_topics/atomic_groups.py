import re

pattern = r"(?>a|ab)c"
text = "abc"
match = re.search(pattern, text)
if match:
    print(f"Matched: {match.group()}")  # Output: None