class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxTotal = float('-inf')
        prevSum = 0

        for n in nums:
            prevSum += n
            if prevSum >= maxTotal:
                maxTotal = prevSum
            if prevSum < 0:
                prevSum = 0
        
        return maxTotal
