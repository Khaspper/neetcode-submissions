class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs: string[]): string[][] {
        const myMap = new Map<string, string[]>
        for (const word of strs) {
            const sortedWord = word.split('').sort().join('')
            if (myMap.has(sortedWord)) {
                myMap[sortedWord] = (myMap.get(sortedWord)).push(word)
            }
            else {
                myMap.set(sortedWord, [word])
            }
        }
        return [...myMap.values()]
    }
}
