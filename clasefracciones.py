class Fraction():
    numerator = 0
    denominator = 1

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        print("mi numerador es ", numerator)
        print("mi denominador es ", denominator)

    def multiply(self, b):
        result_numerator = self.numerator*b.numerator
        result_denominator = self.denominator*b.denominator
        r = Fraction(result_numerator, result_denominator)
        return r

    def add(self, b):
        result_numerator = ((self.numerator*b.denominator) +
                            (b.numerator*self.denominator))
        result_denominator = self.denominator*b.denominator
        r = Fraction(result_numerator, result_denominator)
        return r

    def subtract(self, b):
        result_numerator = ((self.numerator*b.denominator) -
                            (b.numerator*self.denominator))
        result_denominator = self.denominator*b.denominator
        r = Fraction(result_numerator, result_denominator)
        return r

    def divide(self, b):
        result_numerator = self.numerator*b.denominator
        result_denominator = self.denominator*b.numerator
        r = Fraction(result_numerator, result_denominator)
        return r


a = Fraction(4, 10)
b = Fraction(3, 5)
print("multiplicacion")
a.multiply(b)
print("sumatoria")
a.add(b)
print("resta")
a.subtract(b)
print("division")
a.divide(b)
