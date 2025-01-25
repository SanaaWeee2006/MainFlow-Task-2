#  Calculate the Least Common Multiple (LCM) and Greatest Common Divisor (GCD) of two integers.

import math

def calculate_lcm_and_gcd(a, b):
    
    gcd = math.gcd(a, b)
    
    lcm = abs(a * b) // gcd
    return lcm, gcd

a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

lcm, gcd = calculate_lcm_and_gcd(a, b)
print("GCD:", gcd)
print("LCM:", lcm)
