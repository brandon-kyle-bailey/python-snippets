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
    
