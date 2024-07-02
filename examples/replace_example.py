import re

pattern = r"\d+"
text = "There are 123 apples, 45 oranges, and 678 bananas."
result = re.sub(pattern, "number", text)

print(f"Result: {result}")