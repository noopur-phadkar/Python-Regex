import re

pattern = r"\d+"
text = "There are 123 apples, 45 oranges, and 678 bananas."
matches = re.findall(pattern, text)

print(f"Matches: {matches}")