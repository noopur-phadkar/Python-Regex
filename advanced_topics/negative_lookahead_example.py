import re

pattern = r"foo(?!bar)"
text = "foobaz"
match = re.search(pattern, text)

print(f"Matched: {match.group()}")  # Output: "foo"
