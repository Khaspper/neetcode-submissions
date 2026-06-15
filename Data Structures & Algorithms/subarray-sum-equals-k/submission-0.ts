class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number}
     */
    subarraySum(nums: number[], k: number): number {
        const prefix: number = 0
        const myMap = new Map<number, number>; 
        let res: number = 0
        for (const n of nums) {
            const diff: number = prefix - n
            if (myMap.has(diff)) {
                res += myMap.get(diff)
            }
            myMap.set(prefix, (myMap.get(prefix) ?? 0) + 1)
        }

        return res
    }
}
