def camel_to_snake(text):
    result = [text[0].lower()]
    for char in text[1:]:
        if char.isupper():
            result.extend(['_', char.lower()])
        else:
            result.append(char)
    return ''.join(result)

# Example usage
camel_case_string = str(input())
snake_case_string = camel_to_snake(camel_case_string)
print(snake_case_string)