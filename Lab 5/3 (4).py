import re
a=input(str())
x=bool(re.search("[a-z]+_[a-z]",a))
print(x)