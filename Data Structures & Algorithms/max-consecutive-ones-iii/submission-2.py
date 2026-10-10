class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        flip = k
        longest = 0
        count = 0

        for r in range(len(nums)):
            if nums[r] == 1:
                count += 1
                continue
            flip -= 1
            longest = max(longest, count)
            while l < r and flip < 0:
                if nums[l] == 0:
                    flip += 1
                l += 1
                count -= 1
            if flip >= 0:
                count += 1
        
        return max(longest, count)