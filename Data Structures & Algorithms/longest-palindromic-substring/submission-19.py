class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        self.longest = ""

        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                self.longest = self.longest if len(self.longest) > len(s[l: r + 1]) else s[l: r + 1]
                l -= 1
                r += 1

        for i in range(len(s)):
            # Check if it's odd palindrome
            helper(i, i)
            
            # Check if it's odd palindrome
            helper(i, i + 1)
            
        return self.longest