import re
text = input(str(""))
print(re.findall('[A-Z][^A-Z]*', text))