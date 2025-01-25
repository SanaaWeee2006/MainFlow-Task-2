# Reverse a given list without using built-in functions.

def reverse_list(lst):
    
    start = 0
    end = len(lst) - 1
    while start < end:
        
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    return lst

lst = list(map(int, input("Enter a list of integers separated by spaces: ").split()))

print("Reversed list:", reverse_list(lst))
