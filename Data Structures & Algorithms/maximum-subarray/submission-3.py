class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxTotal = nums[0]

        curr = 0
        for n in nums:
            curr = max(curr + n, 0)
            if curr != 0:
                maxTotal = max(curr, maxTotal)
        
        return maxTotal
