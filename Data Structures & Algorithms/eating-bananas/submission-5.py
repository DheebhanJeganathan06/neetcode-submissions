class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minSpeed = r

        while l <= r:
            m = l + ((r - l) // 2)
            time = 0
            for pile in piles:
                time += math.ceil(float(pile) / m)
            if time > h:
                l = m + 1
            else:
                minSpeed = m
                r = m - 1
        return minSpeed


        
        
        