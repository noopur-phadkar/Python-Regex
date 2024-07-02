import re

log = """
2024-06-30 12:00:00,123 - INFO - User logged in
2024-06-30 12:05:00,456 - ERROR - An error occurred
2024-06-30 12:10:00,789 - INFO - User logged out
"""
pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}),\d+ - (\w+) - (.+)"
matches = re.findall(pattern, log)
for match in matches:
    print(f"Timestamp: {match[0]}, Level: {match[1]}, Message: {match[2]}")