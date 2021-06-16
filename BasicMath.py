class BasicMath(object):
    def __init__(self):
        self.a = 5
        self.b = 5.0
        self.n = ''

    def add(self, a, b):
        return self.a + self.b

    def multiply(self, a, b):
        return self.a * self.b

    def subtract(self, a, b):
        return self.a - self.b

    def divide(self, a, b):
        if self.b == 0:
            raise Exception("Any value cant be divided by zero")
        return a / b

    def name(self, n):
        self.n = n
