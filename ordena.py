import os
import re

for file in os.listdir():
    if file.endswith('.log'):
        with open(file) as f:
            content = f.read
            date = re.findall('hola')
