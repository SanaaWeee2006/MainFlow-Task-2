# Find the sum of the digits in a number.

def sum_of_digits(n):
    
    return sum(int(digit) for digit in str(abs(n)))

n = int(input("Enter an integer: "))


print("Sum of digits:", sum_of_digits(n))
