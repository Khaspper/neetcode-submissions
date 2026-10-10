class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        myMap = {}
        count = 0

        for p in people:
            myMap[p] = myMap.get(p, 0) + 1
        
        for p in people:
            if p not in myMap:
                continue

            diff = limit - p

            while diff not in myMap and diff > 0:
                diff -= 1
            
            if diff != 0:
                myMap[diff] -= 1
                if myMap[diff] == 0:
                    del myMap[diff]
            
            if p in myMap:
                myMap[p] -= 1
                if myMap[p] == 0:
                    del myMap[p]

            count += 1

        return count