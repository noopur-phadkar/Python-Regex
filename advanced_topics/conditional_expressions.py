import re

pattern = r"(?(?=\d{4})\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4})"
dates = ["2024-07-02", "02/07/2024"]
for date in dates:
    match = re.match(pattern, date)
    if match:
        print(f"Matched: {date}")