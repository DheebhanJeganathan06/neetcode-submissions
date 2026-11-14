class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # make stone weights negative
        stones = [-s for s in stones]
        # heapify stones so that max is stored at top
        heapq.heapify(stones)

        # iterate on heap while there is more than one element
        while len(stones) > 1:
            # retrieve two largest stones
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            # if the second is less heavy than the first,
            # re-add the first one with the damaged weight
            # if they're both equal, nothing else is added
            # indicating that both were destroyed in battle
            if second > first:
                heapq.heappush(stones, first - second)

        # edge case: if the last two stones destroyed each other,
        # final weight will be 0
        stones.append(0)
        # we return the postive weight of last stone remaining,
        # or 0 if no stones remained
        return abs(stones[0])