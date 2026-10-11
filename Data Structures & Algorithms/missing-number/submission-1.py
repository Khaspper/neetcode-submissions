class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = len(nums)

        for n in range(len(nums)):
            total += n
        
        for i in range(len(nums)):
            total -= nums[i]
        
        return total