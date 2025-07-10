"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""

# The following code doesn't work fully. For complete solution, refer to this code using chatgpt.
def strStr(needle, haystack):
    i = 0
    for char in haystack:
        if i<len(needle) and char == needle[i]:
            i += 1
    if i == len(needle):
            first_char = needle[0]
            index = haystack.find(first_char)
            return index
    else:
            return -1
    
print(strStr("fk","adfkakdjf;lkasjfk"))