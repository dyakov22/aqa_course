

class Calculator:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def divide(self):
        if self.y == 0:
            raise ZeroDivisionError('Could not divide by 0')
        return self.x / self.y

    def multiply(self):
        return self.x * self.y