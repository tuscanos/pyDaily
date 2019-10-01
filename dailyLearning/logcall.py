from functools import wraps

def logged(function):

    # Add logging around the function

    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Calling function: {}".format(function.__name__))
        return function(*args, **kwargs)

    return wrapper
