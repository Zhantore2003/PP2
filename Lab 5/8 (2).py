import re

text = "MyNameIsDulat"

words = re.findall(r'[A-Z][^A-Z]*', text)
print(words)