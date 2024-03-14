import re
a=input(str())
x=bool(re.search("^a.*?b$",a))
print(x)