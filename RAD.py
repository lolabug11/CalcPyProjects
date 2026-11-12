from math import sqrt
class Number:
    @staticmethod
    def get_factors(number):
        if number != 1:
            current_factor_test = 1
            factors = []
            while sqrt(number) > current_factor_test:
                if number % current_factor_test == 0:
                    factors.append(current_factor_test)
                    factors.append(number/current_factor_test)
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
            return Number(outer*inner.root)
        return Number([outer,inner])

    def mult(self,num:Number):
        """
        :param num:
        Number Object
        :return:
        Number Object
        """
        # Checks if the parts of the operations are radical expressions
        if self.isRadicalExpression and num.isRadicalExpression:
            """
            If they are both radical expressions:
            multiply one outer by the other, multiply one inner by the inner
            Simplify the radical expression it creates and return a new Number object
            """
            outer = self.number[0] * num.number[0]
            inner = self.number[1] * num.number[1]
            result = Number.simplify_radical(outer,inner)
            return Number(result.number)
        elif self.isRadicalExpression and not num.isRadicalExpression:
            """
            if self is a radical expression but num isn't:
            multiply self's outer by num and set inner to self's inner
            Simplify the radical expression it creates and return a new Number object
            """
            outer = self.number[0] * num.number
            inner = self.number[1]
            result = Number.simplify_radical(outer,inner)
            return Number(result.number)
        elif not self.isRadicalExpression and num.isRadicalExpression:
            """
            If num is a radical expression but self isn't:
            multiply self by num's outer, set inner to num's inner
            Simplify the radical expression it creates and return a new Number object
            """
            outer = self.number * num.number[0]
            inner = num.number[1]
            result = Number.simplify_radical(outer,inner)
            return Number(result.number)
        else:
            """
            Otherwise:
            multiply self by num and return a Number object
            """
            result = self.number * num.number
            return Number(result)

    def add(self,num:Number):
        """
        :param num:
        Number Object
        :return:
        Number Object or None, Number object if the addition is valid, None if not
        """
        if self.isRadicalExpression and num.isRadicalExpression:
            """
            If both self and num are radical expressions:
            check if their radicans are the same add the coefficents
            return a Number object of the result
            """
            if self.number[1] == num.number[1]:
                outside = self.number[0] + num.number[0]
                inside = self.number[1]
                return Number([outside, inside])
        elif not self.isRadicalExpression and not num.isRadicalExpression:
            """
            If self and num are not radical expressions:
            return the sum of the 2 numbers
            """
            return self.number + num.number
        return None

    def __init__(self,number:list[int]|int):
        if type(number) == list:
            self.isRadicalExpression = True
            self.number = number
            self.isPrime = False
            self.isPerfectSquare = False
            self.factors = None
        else:
            self.isRadicalExpression = False
            self.number = number
            self.isPrime = Number.is_prime(number)
            self.isPerfectSquare = Number.is_perfect_square(number)
            self.factors = Number.get_factors(number)
            if self.isPerfectSquare:
                self.root = sqrt(number)

    def __str__(self):
        if self.isRadicalExpression:
            return str(self.number[0]) + " * sqrt(" + str(self.number[1]) + ")"

        return str(self.number)
"Testing for simplifying radicals and what the calculator version runs:"
# while True:
#     coeff = int(input("What is the coefficent of your radical expression?\n> "))
#     radican = int(input("What is the radican of your radical expression?\n> "))
#     print( Number.simplify_radical(coeff, radican))
""" Testing for Number object Mulplification"""
number1 = Number([2,3])
number2 = Number([2,4])
number3 = number1.add(number2)
print(number3)
