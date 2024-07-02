import re

pattern = r"(?P<first_name>\w+) (?P<last_name>\w+)"
text = "John Doe"
match = re.match(pattern, text)
if match:
    print(match.group("first_name"))  # Output: "John"
    print(match.group("last_name"))   # Output: "Doe"