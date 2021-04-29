# inheritance
class Vehicle:
    pass

class Bicycle(Vehicle):
    pass

# composition
class Engine:
    pass

class Car:
    def __init__(self):
        self.engine = Engine()
