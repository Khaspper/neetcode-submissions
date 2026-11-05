class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums = set(nums)
        longest = 0

        for n in nums:
            if n - 1 in nums:
                continue
            
            count = 1
            while n + 1 in nums:
                count += 1
                n += 1
            longest = max(count, longest)
        return longest