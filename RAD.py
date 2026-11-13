from math import sqrt
class Number:
    @staticmethod
    def get_factors(number):
        # initalize the factor list with one because every number has one as a factor
        factors = [1]
        if number != 1:
            # if the number isn't one set the current factor test to 2 because one is alredy defined as a factor
            current_factor_test = 2
            """
            While the sqrt of the number is greater than the  current factor test
            you use the square root of the number to cut down the amount of itterations that the loop has to do
            this dosent skip any factors because they are just the oteh
            """
            while sqrt(number) > current_factor_test:
                """
                number % current_factor_test == 0: is checking if number/current_factor test is a whole number
                if it is a number that means current_factor_test is a factor of number
                """
                if number % current_factor_test == 0:
                    # add the current_factor_test to the list of factors then add the number/current_factor_test to the list of factors
                    factors.append(current_factor_test)
                    factors.append(number/current_factor_test)
                # increment current_factor_test by one so the loop checks a new number
                current_factor_test += 1
            return factors
        return factors

    @staticmethod
    def is_prime(number):
        # if all the factor list of number only has one in it set it to prime
        if Number.get_factors(number) == [1]:
            return True
        return False

    @staticmethod
    def is_perfect_square(number):
        # if the squar of number has a .000 set it to be a perfect square
        square = sqrt(number)
        if ".000" in (str(square) + "000"):
            return True
        return False

    @staticmethod
    def simplify_radical(outer, inner):
        """
        :arg outer:
        a whole number that is the outside part of a radical expression
        :arg inner:
        a whole number that is the radican of a radical expression
        :return:
        a Number object that is a radical expression
        """
        #set inner to a Number object with the value of the passed inner var
        inner = Number(inner)
        while not inner.isPrime and not inner.isPerfectSquare:
            # set factors to the factors of the inner object
            factors = inner.factors
            # initialize perfect_square_factor to None
            perfect_square_factor = None
            for factor in factors:
                # for every factor in the list of factors
                if factor != 1 and Number(factor).isPerfectSquare :
                    # if the factor isn't one and it's a perfect square set perfect_square_factor to that factor and break the loop
                    perfect_square_factor = factor
                    break
            if perfect_square_factor is not None:
                # set the inner to the new inner with the perfect square factor taken out
                inner = Number(inner.number/perfect_square_factor)
                # set outer to outer times the sqaure root of the perfect square factor
                outer *= sqrt(perfect_square_factor)
            else:
                break
        if inner.isPerfectSquare:
            #if the inner number is a perfect square reuturn a whole number Number object containing the outer number times the root of the inner number
            return Number(outer*inner.root)
        # otherwise return a radical expression Number object
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

    def sub(self,num:Number):
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
                outside = self.number[0] - num.number[0]
                inside = self.number[1]
                return Number([outside, inside])
        elif not self.isRadicalExpression and not num.isRadicalExpression:
            """
            If self and num are not radical expressions:
            return the sum of the 2 numbers
            """
            return self.number - num.number
        return None

    def __init__(self,number:list[int]|int):
        """
        :param number:
        If the number is a radical expression input a list of 2 ints
        outer * sqrt(inner): [outer, inner]
        """

        if type(number) == list:
            # if the number input is a list that means it's a radical expressesion so set it to that
            self.isRadicalExpression = True
            # set the number to the list that was passed
            self.number = number
            # radical expressions cant be prime so set it to false
            self.isPrime = False
            # radical expressions cant  be perfect squares so set it to false
            self.isPerfectSquare = False
            # radical expressions cant have factors so set factors to None
            self.factors = None
        else:
            # the input was not a list it was an int so set isRadicalExpressions to false
            self.isRadicalExpression = False
            # set number to the number that was passed
            self.number = number
            # if the number passed is prime set isPrime to true otherwise set it to false
            self.isPrime = Number.is_prime(number)
            # if the number is a perfect square set isPerfectSquare to true otherwise set it to false
            self.isPerfectSquare = Number.is_perfect_square(number)
            # set the factors attribute to the factors of the number
            self.factors = Number.get_factors(number)
            if self.isPerfectSquare:
                # if the number is a perfect square set root to the sqrt of the number
                self.root = sqrt(number)

    def __str__(self):
        if self.isRadicalExpression:
            # if the number is a radical expression return a string that looks like this
            # "outer * sqrt(inner)"
            return str(self.number[0]) + " * sqrt(" + str(self.number[1]) + ")"
        # otherwise just return the number as a string
        return str(self.number)

"Testing for simplifying radicals and what the calculator version runs:"
# while True:
#     coeff = int(input("What is the coefficent of your radical expression?\n> "))
#     radican = int(input("What is the radican of your radical expression?\n> "))
#     print( Number.simplify_radical(coeff, radican))
""" Testing for Number object Mulplification"""
number1 = Number([2,3])
number2 = Number([3,3])
number3 = number1.sub(number2)
print(number3)


""" Possible additions
1. If outside of the radical expression is 0 then set the Number object to a non radical expression int
"""