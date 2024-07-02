import re

pattern = r"^\+?\d{1,4}[-.\s]?$begin:math:text$?\\d{1,3}$end:math:text$?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"
phone_number = "+1-800-555-1234"
if re.match(pattern, phone_number):
    print("Valid phone number")
else:
    print("Invalid phone number")