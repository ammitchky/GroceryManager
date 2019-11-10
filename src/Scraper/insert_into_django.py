import json
with open('data', 'r') as f:
    items = json.load(f.read().replace(r'\u2014', '-'))

# First, merge items together
