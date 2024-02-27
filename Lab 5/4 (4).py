import re

pattern = re.compile(r"[A-Z]{1}[a-z]+")
print(pattern.findall("Dulat Sultanbek programming Principles 2"))
