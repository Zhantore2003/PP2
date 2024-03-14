import re
text = input(str(""))
replacedText = re.sub('[ ,.]', ':', text)
print(replacedText)
