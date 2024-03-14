import re
a=input(str())
x=bool(re.search("^[A-Z][a-z]+",a))
print(x)