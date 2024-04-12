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

def main():
    try:
        # Taking input from the user
        a = int(input("Enter the first positive integer: "))
        b = int(input("Enter the second positive integer: "))
        
        # Checking if the inputs are valid
        if a <= 0 or b <= 0:
            raise ValueError("Both numbers must be positive integers.")
        
        # Calculating GCD
        gcd_calculator = EuclideanAlgorithm()
        result = gcd_calculator.gcd(a, b)
        print(f"The GCD of {a} and {b} is {result}")
    except ValueError as e:
        print(f"Invalid input: {e}")

main()
