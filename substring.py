#TODO: given a string 's'find the length of the longest substring without duplicate characters

"""
Eg:
    Input: s = "abcabcbb"
    Output: 3
    Explination: The answer is "abc" with the length of 3 

Eg:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Constraints:
    -> 0 <= s,length <=5 *10 ^4
    -> 's' consists of english letters,digits,symbols and spaces 
Hint: 
    Generate all possible substrings & check for each substring if its valid and keep updating 'maxLen' accordingly.
"""

def lengthOfSubstring(s):
    n=len(s)
    maxLength=0
    charIndex=[-1]*128
    left=0

    for right in range(n):
        if charIndex[ord(s[right])]>=left:
            left=charIndex[ord(s[right])]+1
        charIndex[ord(s[right])]=right
        maxLength=max(maxLength,right-left+1)
        print("pwwkew")
    return maxLength

