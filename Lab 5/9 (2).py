import re
def insert_spaces(text):
    pattern = r'(?<=[a-z])(?=[A-Z])'
    result = re.sub(pattern, ' ', text)
    return result
text = input(str(""))
result = insert_spaces(text)
print(result)