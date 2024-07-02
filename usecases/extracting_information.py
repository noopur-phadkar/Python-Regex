import re

text = "The price of the item is $45.99 and the tax is $3.50."
pattern = r"\$\d+\.\d{2}"
prices = re.findall(pattern, text)
print(f"Prices found: {prices}")  # Output: ["$45.99", "$3.50"]