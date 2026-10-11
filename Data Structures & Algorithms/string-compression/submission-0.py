class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        count = 0
        for r in range(len(chars)):
            if chars[r] == chars[l]:
                count += 1
                continue
            if count == 1:
                l += 1
                count = 0
                continue
            s = list(chars[l] + str(count))
            print(f"s: {s}")
            count = 0
            for c in s:
                chars[l] = c
                l += 1
        print(chars)
        print(count)
        print(f"l: {l}")
        print(f"r: {r}")

        if l != r:
            print(f"L does not equal to R")
            s = list(chars[l] + str(count))
            print(f"s: {s}")
            for c in s:
                chars[l] = c
                l += 1
            l -= 1




        return l + 1