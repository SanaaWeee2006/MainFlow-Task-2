# Count the number of vowels and consonants in a string.

def count_vowels_and_consonants(s):
    vowels = set("aeiouAEIOU")  # Set of vowels
    vowel_count = 0
    consonant_count = 0

    for char in s:
        if char.isalpha():  # Check if the character is a letter
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count

# Input: A string
s = input("Enter a string: ")

# Count vowels and consonants
vowels, consonants = count_vowels_and_consonants(s)

# Output: Count of vowels and consonants
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
