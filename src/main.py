# factorial.py

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    
    The factorial of n (denoted as n!) is defined as:
    - n! = 1 when n = 0
    - n! = n * (n-1) * (n-2) * ... * 1 when n > 0
    
    Parameters:
        n (int): A non-negative integer
    
    Returns:
        int: The factorial of n
    """
    # TODO: Implement the factorial logic here
    pass

# Testing the function
if __name__ == "__main__":
    try:
        # Example: Replace 5 with other values to test
        number = int(input("Enter a non-negative integer: "))
        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print(f"The factorial of {number} is {factorial(number)}")
    except ValueError:
        print("Please enter a valid integer.")
