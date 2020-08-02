#!/usr/bin/env python3
import re


text = '''

'''

pattern = re.compile(r'(\bDoe\b)')
matches = pattern.finditer(text)
for match in matches:
    print(match)
