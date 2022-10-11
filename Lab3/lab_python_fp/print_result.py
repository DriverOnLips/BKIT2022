# DONE


def print_result(func):
    def wrapper(param):
        print(func.__name__)
        result = func(param)
        print(result)
        return result
    return wrapper
