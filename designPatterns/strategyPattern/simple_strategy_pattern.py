#/usr/bin/env python3


class Fly:
    @staticmethod
    def fly() -> str:
        return "Flying object"

class Quack:
    @staticmethod
    def quack() -> str:
        return "Quacking object"

class Display:
    @staticmethod
    def display() -> str:
        return "Displaying object"

class Duck:
    def __init__(self, fb, qb, db) -> None:
        self.fb = fb
        self.qb = qb
        self.db = db

if __name__ == "__main__":

    myDuck = Duck(fb=Fly, qb=Quack, db=Display)

    print(myDuck, end="\n\n")

    print(myDuck.fb, end="\n\n")
    print(myDuck.db, end="\n\n")
    print(myDuck.qb, end="\n\n")

    print(myDuck.fb.fly(), end="\n\n")
    print(myDuck.qb.quack(), end="\n\n")
    print(myDuck.db.display(), end="\n\n")
    
