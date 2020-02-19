#!/usr/bin/env python3

# base.py
class Base:
    def __init__(self):
        self.baseFunc()
    def __init_subclass__(cls, *args, **kwargs):
        print(f"initializing {cls} from Base.")
        assert hasattr(cls, "derivedFunc"), f"{cls} does not have a function 'derivedFunc'"
        return super().__init_subclass__(*args, **kwargs)
    def baseFunc(self):
        print(f"{self} called baseFunc")
      
# dervied.py
from base import Base
assert hasattr(Base, "baseFunc"), f"{Base} does not have a function 'baseFunc'"
class Derived(Base):
    def __init__(self):
        print(f"{self} initialized")
        self.derivedFunc()
    def derivedFunc(self):
        print(f"{self} called derivedFunc")
        
if __name__ == "__main__":

    derived = Derived()
