class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        longest = ""

        def helper(l, r) -> str:
            if l >= 0 and r < len(s) and s[l] != s[r]:
                return ""
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1
            return s[l: r]

        for i in range(len(s)):
            # Check if it's odd palindrome
            currLongest = helper(i, i)
            
            # Check if it's odd palindrome
            temp = helper(i, i + 1)

            if len(currLongest) < len(temp):
                currLongest = temp
            if len(currLongest) > len(longest):
                longest = currLongest

            
        return longest