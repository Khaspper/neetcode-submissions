class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums: number[], k: number): number[] {
        const myMap = new Map<number, number>();

        for (const n of nums) {
            if (myMap.has(n)) {
                myMap.set(n, myMap.get(n) + 1)
            } else {
                myMap.set(n, 1)
            }
        }

        const sortedMap = [...myMap.entries()].sort((a, b) => b[1] - a[1])
        const res = []
        for (let i = 0; i < k; i += 1) {
            res.push(sortedMap[i][0])
        }
        return res
    }
}
