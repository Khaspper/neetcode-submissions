class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        //? <element, index>
        const myMap = new Map<number, number>()

        for (let i = 0; i < nums.length; i += 1) {
            const diff = target - nums[i]
            if (myMap.has(diff)) {
                const res: number[] = [myMap.get(diff), i]
                return res
            }
            myMap.set(nums[i], i)
        }
        return []
    }
}
