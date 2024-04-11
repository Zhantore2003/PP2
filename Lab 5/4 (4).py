import re
a=input(str())
x=bool(re.search("^.@gmail.com&",a))
print(x)