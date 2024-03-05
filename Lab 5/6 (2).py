import re

text = "Hello My name, is. Dulat"
replacedText = re.sub(r'[ ,.]', ':', text)
print(replacedText)