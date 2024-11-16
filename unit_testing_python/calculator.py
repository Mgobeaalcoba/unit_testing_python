class Calculator: # With Doctests in the class
    @staticmethod
    def add(a, b):
        """
        >>> Calculator.add(1, 2)
        3
        >>> Calculator.add(10, 20)
        30
        >>> Calculator.add(1, -1)
        0
        """
        return a + b

    @staticmethod
    def subtract(a, b):
        """
        >>> Calculator.subtract(1, 2)
        -1
        >>> Calculator.subtract(10, 20)
        -10
        >>> Calculator.subtract(1, -1)
        2
        """
        return a - b

    @staticmethod
    def multiply(a, b):
        """
        >>> Calculator.multiply(1, 2)
        2
        >>> Calculator.multiply(10, 20)
        200
        >>> Calculator.multiply(1, -1)
        -1
        """
        return a * b

    @staticmethod
    def divide(a, b):
        """
        >>> Calculator.divide(1, 2)
        0.5
        >>> Calculator.divide(10, 20)
        0.5
        >>> Calculator.divide(1, -1)
        -1.0
        >>> Calculator.divide(1, 0)
        0
        """
        if b != 0:
            return a / b
        else:
            return 0

    @staticmethod
    def unsafe_divide(a, b):
        """
        >>> Calculator.unsafe_divide(1, 2)
        0.5
        >>> Calculator.unsafe_divide(10, 20)
        0.5
        >>> Calculator.unsafe_divide(1, -1)
        -1.0
        >>> Calculator.unsafe_divide(1, 0)
        Traceback (most recent call last):
        ZeroDivisionError: division by zero
        """
        return a / b
