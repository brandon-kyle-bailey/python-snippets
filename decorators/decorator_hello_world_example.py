#!/usr/bin/env python


# define function to be used as the decorator.
def custom_decorator(func):
    """Decorator function to perform some logic before and after
    the decorated function is executed.

    This is a perfect example of a factory.
    A function that returns another function.

    Args:
        func: (function) object of inner function to execute.

    Returns:
        wrapper: (function) of wrapper function to execute.
    """
    def wrapper(*args, **kwds):
        """Wrapper function is the function that wraps around
        the function to execute. It consumes any args and
        key word args and parses them back in to the function
        on call.

        Args:
            *args: (arguments) object of any non key word arguments.
            **kwargs: (arguments) object of key word arguments.
        """

        print("Running pre inner function logic.")

        # execute the function with the consumed args and kwargs.
        result = func(*args, **kwds)

        print("Running post inner function logic.")

        return result

    return wrapper


# decorator is provided with the @ syntax above the
# function (subject) definition.
@custom_decorator
def hello_world():
    """Function that executes some logic.
    """

    print("Hello world, this is my first decorator function")


if __name__ == "__main__":
    hello_world()
    
