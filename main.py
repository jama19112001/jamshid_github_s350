def calculate_factorial(n):
    """Returns the factorial of a positive integer."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result