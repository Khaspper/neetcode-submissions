class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        flip = k
        longest = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                flip -= 1
            while flip < 0:
                if nums[l] == 0:
                    flip += 1
                l += 1
            longest = max(longest, r - l + 1)
        
        return longest