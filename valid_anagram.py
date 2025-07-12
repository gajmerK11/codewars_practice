"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""

# This code is my code revised by chatgpt
def isAnagram(s,t):
    # This is length check. This checks if both strings have the same number of characters. If they don't, it's impossible for them to be anagrams — so we immediately return False.
    if len(s) != len(t):
        return False
    
    #  This loop: 
    # 1. Checks if each character in s is present in t, and     
    # 2. Removes that character from t's list, so repeated letters are handled properly.
    list2 = list(t)
    for char in s:
        if char in list2:
            list2.remove(char)
        else:
            return False
    return True


# # From chatgpt
# from collections import Counter
# def isAnagram(s,t):
#     return Counter(s) == Counter(t)
# print(isAnagram("aacc","ccca"))