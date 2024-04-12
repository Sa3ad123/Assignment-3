class EuclideanAlgorithm:
    """
    A class to implement the Euclidean Algorithm for computing the greatest common divisor (GCD)
    of two integers.
    """
    
    @staticmethod
    def gcd(a, b):
        """
        Static method to calculate the GCD of two numbers using the Euclidean Algorithm.
        
        Parameters:
        a (int): First integer
        b (int): Second integer, should not be greater than 'a'
        
        Returns:
        int: The greatest common divisor of 'a' and 'b'
        """
        while b != 0:
            a, b = b, a % b
        return a


gcd_calculator = EuclideanAlgorithm()
a = 270
b = 192
print(f"The GCD of {a} and {b} is {gcd_calculator.gcd(a, b)}")
