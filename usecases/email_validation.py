import re

pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
email = "example@example.com"
if re.match(pattern, email):
    print("Valid email address")
else:
    print("Invalid email address")