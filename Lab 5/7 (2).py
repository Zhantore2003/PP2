def snake_to_camel(snake_case_str):
    words = snake_case_str.split('_')
    camel_case_words = [words[0]] + [word.capitalize() for word in words[1:]]
    return ''.join(camel_case_words)
snake_case_str = input(str(""))
camel_case_str = snake_to_camel(snake_case_str)
print(camel_case_str)