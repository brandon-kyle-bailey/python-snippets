#!/usr/bin/env python3


def color_text_decorator(func):
    """Decorator function to change color of text of input
    function.
    Args:
        func: (function): input function.
    Returns:
        wrapper: function with input function wrapped.
    """

    def wrapper(*args, **kwargs):
        """Wrapper function to return from decorator
        with appropriate logic.
        Args:
            *args: arguments from input function
            **kwargs: key word arguments from input function
        Returns:
            func: returns function with args and kwargs
        """

        args = ['\033[93m'+arg+'\033[0m' for arg in args]
        return func(*args, **kwargs)

    return wrapper


@color_text_decorator
def cprint(*args):
    """Print n number of input string.
    Args:
        *args: string arguments to input.
    """

    for arg in args:
        print(arg, end=" ")
    print("")


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
    def wrapper(*args, **kwargs):
        """Wrapper function is the function that wraps around
        the function to execute. It consumes any args and
        key word args and parses them back in to the function
        on call.
        Args:
            *args: (arguments) object of any non key word arguments.
            **kwargs: (arguments) object of key word arguments.
        """


        from timeit import default_timer

        start = default_timer()
        cprint("Running wrapper function.")
        # execute the function with the consumed args and kwargs.
        result = func(*args, **kwargs)
        cprint(f"Process executed in {default_timer() - start}")

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

#================================================================================
#================================================================================

#!/usr/bin/env python3


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


        from timeit import default_timer

        start = default_timer()

        print("Running pre inner function logic.")
        # execute the function with the consumed args and kwargs.
        result = func(*args, **kwds)
        print("Running post inner function logic.")

        print(f"Process executed in {start - default_timer()}")

        return result

    return wrapper


# decorator is provided with the @ syntax above the
# function (subject) definition.
@custom_decorator
def hello_world():
    """Function that executes some logic.
    """

    import time

    time.sleep(10)
    print("Hello world, this is my first decorator function")


if __name__ == "__main__":
    hello_world()
