#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Context:
    def __init__(self, strategy):
        self._strategy = strategy
    @property
    def strategy(self):
        return self._strategy
    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy
    def do_some_business_logic(self, *args, **kwargs):
        print("Context: Sorting data using a strategy.")
        return self._strategy.do_algorithm(*args, **kwargs)
        
class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, *args, **kwargs):
        pass

class ConcreteStrategyA(Strategy):
    def do_algorithm(self, *args, **kwargs):
        if args:
            for arg in args:
                yield sorted(arg)
        if kwargs:
            for key, arg in kwargs.items():
                yield (key, arg)
                
class ConcreteStrategyB(Strategy):
    def do_algorithm(self, *args, **kwargs):
        if args:
            for arg in args:
                yield sorted(arg, reverse=True)
        if kwargs:
            for key, arg in kwargs.items():
                yield (key, arg)    
                
if __name__ == "__main__":

    context = Context(ConcreteStrategyA())
    print("Client: Strategy is set to normal sorting.")
    for item in context.do_some_business_logic([1,2,3,4,5]):
        print(item, end="\n\n")
        
    context.strategy = ConcreteStrategyB()
    print("Client: Strategy is set to reverse sorting.")
    for item in context.do_some_business_logic([1,2,3,4,5]):
        print(item, end="\n\n")    

    
