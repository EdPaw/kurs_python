import time


def timepassed(function):
    def nested():
        start_time = time.time()
        function()
        end_time = time.time()

        execution_time = end_time - start_time
        return execution_time

    return nested

@timepassed
def get_text_1():
    x = input("Podaj ulubione danie-> ")
    print("ALE DŁUGO")


print(get_text_1())
