class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums: number[]): number[] {
        const res: number[] = nums
        res.push(...nums)
        return nums
    }
}
