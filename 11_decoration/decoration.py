def uppercase_decorator(function):
    def nested():
        result = function()
        return result.upper()

    return nested

@uppercase_decorator
def get_text_1():
    return "abcgfygbufik"

@uppercase_decorator
def get_text_2():
    return "text 2"


result = get_text_2()
print(result)

result = get_text_1()
print(result)