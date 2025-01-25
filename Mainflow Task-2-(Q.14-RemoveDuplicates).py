#  Remove duplicate elements from a list

def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)  # Add only unique elements
    return unique_list

# Input: List of integers
lst = list(map(int, input("Enter a list of integers separated by spaces: ").split()))

# Output: List with unique elements
print("List with unique elements:", remove_duplicates(lst))
