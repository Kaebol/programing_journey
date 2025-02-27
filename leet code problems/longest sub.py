class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    charSet = set()    
    1 = 0 

    for r in range (len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])