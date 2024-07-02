import re

text = "The color of the car is blue."
pattern = r"blue"
replacement = "red"
new_text = re.sub(pattern, replacement, text)
print(new_text)  # Output: "The color of the car is red."