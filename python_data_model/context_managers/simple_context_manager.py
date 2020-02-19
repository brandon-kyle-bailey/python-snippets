#!/usr/bin/env python


class BasicContextManager():

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        return self.name

    def __exit__(self, exc_type, exc_value, traceback):
        return self.name


if __name__ == "__main__":

    print("This is before the context manager.")
    
    with BasicContextManager("Hello world, this is a context manager.") as data:
        print('\033[93m' + data + '\033[0m')
    
    print("This is after the context manager.")
    
    
#===================================================================================
#===================================================================================

from contextlib import contextmanager

@contextmanager
def myContextManager(data):
    """Context manager which functions identically to the
    one above. Except this has been created using contextlib.
    Contextmanager in this scenario must be a generator (yield).
    
    Args:
        data: input data to use during context.
       
    yields:
        data
    """
    
    yield data
    
if __name__ == "__main__":

    with myContextManager("This is a context manager created using contextlib.") as example:
        print("\033[93m" + example + "\033[0m")

