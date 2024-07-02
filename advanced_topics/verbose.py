import re

pattern = re.compile(r"""
    \d{3} # Area code
    -     # Separator
    \d{3} # First three digits
    -     # Separator
    \d{4} # Last four digits
""", re.VERBOSE)

text = "Call me at 123-456-7890"
match = re.search(pattern, text)
if match:
    print(f"Phone number found: {match.group()}")