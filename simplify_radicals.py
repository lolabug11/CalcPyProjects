from math import sqrt

class Number:
    @staticmethod
    def get_factors(number):
        if number != 1:
            current_factor_test = 1
            factors = []
            while number > current_factor_test:
                if number % current_factor_test == 0:
                    factors.append(current_factor_test)
                current_factor_test += 1
            return factors
        return [1]

    @staticmethod
    def is_prime(number):
        if Number.get_factors(number) == [1]:
            return True
        return False

    @staticmethod
    def is_perfect_square(number):
        square = sqrt(number)
        if ".000" in (str(square) + "000"):
            return True
        return False

    @staticmethod
    def simplify_radical(outer, inner):
        inner = Number(inner)
        while not inner.isPrime and not inner.isPerfectSquare:
            factors = inner.factors
            perfect_square_factor = None
            for factor in factors:
                if factor != 1 and Number(factor).isPerfectSquare :
                    perfect_square_factor = factor
                    break
            if perfect_square_factor is not None:
                inner = Number(inner.number/perfect_square_factor)
                outer *= sqrt(perfect_square_factor)
            else:
                break
        if inner.isPerfectSquare:
            return str(outer*inner.root)
        return str(outer) + " * sqrt(" + str(inner) + ")"


    def __init__(self,number):
        self.number = number
        self.isPrime = Number.is_prime(number)
        self.isPerfectSquare = Number.is_perfect_square(number)
        self.factors = Number.get_factors(number)
        if self.isPerfectSquare:
            self.root = sqrt(number)

    def __str__(self):
        return str(self.number)

while True:
    coeff = int(input("What is the coefficent of your radical expression?\n> "))
    radican = int(input("What is the radican of your radical expression?\n> "))
    print(Number.simplify_radical(coeff,radican))