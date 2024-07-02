import re

config = """
[database]
host = localhost
port = 5432
user = admin
password = secret
"""
pattern = r"(\w+)\s*=\s*(.+)"
matches = re.findall(pattern, config)
config_dict = {key: value for key, value in matches}
print(config_dict)