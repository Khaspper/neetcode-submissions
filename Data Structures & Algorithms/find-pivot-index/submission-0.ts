class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    pivotIndex(nums: number[]): number {
        let left: number = 0;
        let right: number = nums.reduce((acc, curr) => acc + curr, 0)

        for (let i = 0; i < nums.length; i++) {
            right -= nums[i]
            if (right === left) return i
            left += nums[i]
        }
        return -1
    }
}
