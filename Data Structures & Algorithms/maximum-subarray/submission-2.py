class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSubarraySum = float('-inf')
        prevSum = 0

        for n in nums:
            total = n + prevSum
            if total >= n:
                prevSum = total
            else:
                prevSum = n
            maxSubarraySum = max(maxSubarraySum, prevSum)
        return maxSubarraySum