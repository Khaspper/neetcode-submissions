class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        longest = ""

        for i in range(len(s)):
            # Check if it's odd palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                longest = longest if len(longest) > len(s[l: r + 1]) else s[l: r + 1]
                l -= 1
                r += 1
            
            # Check if it's odd palindrome
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                longest = longest if len(longest) > len(s[l: r + 1]) else s[l: r + 1]
                l -= 1
                r += 1
            
        return longest