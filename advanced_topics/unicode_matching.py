import re

pattern = r"\p{L}+"  # Matches any kind of letter from any language
text = "こんにちは world 你好"
matches = re.findall(pattern, text)
print(matches)  # Output: ['こんにちは', 'world', '你好']