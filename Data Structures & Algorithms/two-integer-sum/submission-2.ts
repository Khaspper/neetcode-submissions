class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        const myMap = new Map<number, number>()
        for (let i = 0; i < nums.length; i++) {
            const diff = target - nums[i]
            myMap.set(nums[i],i)
        }
        console.log(myMap)
        return []
    }
}
