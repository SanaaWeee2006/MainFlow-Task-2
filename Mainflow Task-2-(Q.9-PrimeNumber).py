# Prime -- > no. is divisible by 1 and itself

# <------ METHOD - 1 (using for loop)------->
# def prime_check(number):

#     for i in range(2, number):
#         if number % i == 0:
#             print(f"{number} is not a prime num")
#     else:
#         print(f'{number} is a prime')
            

# number = int(input("Enter num : "))

# prime_check(number)

# <------ METHOD - 2 ------->

import math

n = int(input('Enter num : '))

def prime_check(n):

    if n > 1:

        for i in range(n, math.ceil((n/2)+1)):

            if n % i == 0:
                print(f"{n} is not prime")
                break
        else:
            print(f'{n} is prime')
    else:
        print(f'{n} is not prime')

prime_check(n)
