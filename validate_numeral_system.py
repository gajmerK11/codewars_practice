# Question
# A numeral system is a way of writing numbers using a specific set of digits: for example, the decimal system (also called base-10), which is the most commonly used numeral system worldwide, uses the digits 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 to represent numbers. There is also the binary system (also called base-2), which uses the digits 0 and 1.

# For digits that are bigger than 9, the English alphabet is used: 'A' is used for the number 10 in bases higher than 10. This goes all the way to 'Z' in base-36.

# The largest digit allowed in a certain base is always 1 smaller than this base.

# You need to write a function that checks whether all of the digits of a non-negative integer number are a part of the specified base: for example, the number 17253 is valid for base-8, because this base contains the digits 0, 1, 2, 3, 4, 5, 6, 7, but the number 19823 is not valid for this base, because it contains the digits 9 and 8 which are not a part of base-8.

# Note: numbers will be checked against bases from 2 to 36. For digits > 9 (A, B, etc.) such digits will always be uppercase. The function should return a boolean: true for numbers that are valid for a specified numeral system and false otherwise.


import string

def validate_base(num:str, base:int) -> bool:
    # Ensure base is within the valid range
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
    
    # Get allowed characters for the base
    digits = string.digits + string.ascii_uppercase # '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    allowed_digits_in_base = digits[:base]

    # Check each character in the number
    for char in num:
        if char.upper() not in allowed_digits_in_base:
            return False
        
    return True
        
   

print(validate_base('ABC',12))


# 🔷 Summary of the Logic
# "To determine if a number is valid in a specific base, build the list of allowed characters for that base by slicing from a standard list of digits and letters. Then, check whether every character in the number belongs to that list. If any character isn’t allowed in that base, the number is invalid."

