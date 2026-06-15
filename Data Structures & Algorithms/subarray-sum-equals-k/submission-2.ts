class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number}
     */
    subarraySum(nums: number[], k: number): number {
        let prefix: number = 0
        const myMap = new Map<number, number>; 
        myMap.set(0, 1)
        let res: number = 0
        for (const n of nums) {
            prefix += n
            const diff: number = prefix - k
            if (myMap.has(diff)) {
                res += myMap.get(diff)
            }
            myMap.set(prefix, (myMap.get(prefix) ?? 0) + 1)
        }
        return res
    }
}
