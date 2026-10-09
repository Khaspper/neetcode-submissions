class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # first step loop through the array and check if the word starts and ends with a vowel
        # add the sum
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        res = []
        total = 0

        for i in range(len(words)):
            word = words[i]
            if word[0] in vowels and word[-1] in vowels:
                total += 1
            words[i] = total
        
        for i in range(len(queries)):
            start, end = queries[i]
            res.append(words[end] - (words[start - 1] if start > 0 else 0))

        return res