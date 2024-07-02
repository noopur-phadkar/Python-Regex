import re

pattern = r"foo(?=bar)"
text = "foobar"
match = re.search(pattern, text)

print(f"Matched: {match.group()}")  # Output: "foo"
