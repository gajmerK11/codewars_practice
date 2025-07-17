"""
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false

Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice."""

def repeatedSubstringPattern(s: str) -> bool:
    # Get the length of the input string
    n = len(s)

    # Try all possible substring lengths from 1 to half the length of the string
    #  i represents the length of the candidate substring we’re testing.
    # Here we only check up to n // 2 because any valid repeating substring must be short enough to occur at least twice in the full string.
    for i in range(1, n//2 + 1):
        # Only check substring lengths that divide the full string evenly
        if n % i == 0:
            # Take the substring of length i from the start of the string
            substring = s[:i]
            # Repeat the substring enough times to reach the full length of s
            repeated = substring * (n//i)
            # Check if the repeated string matches the original
            if repeated == s:
                return True

    return False

print(repeatedSubstringPattern("aba"))

