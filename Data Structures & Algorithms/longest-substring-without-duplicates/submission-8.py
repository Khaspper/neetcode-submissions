class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        
        if len(s) == 0:
            return 0
        
        mySet = set()
        l = 0

        for r in range(len(s)):
            while l < r and s[r] in mySet:
                mySet.remove(s[l])
                l += 1
            mySet.add(s[r])
            longest = max(longest, r - l)
        
        return longest + 1

