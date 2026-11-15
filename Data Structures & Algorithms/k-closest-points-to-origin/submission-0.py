class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closestPoints = []

        for i,(x,y) in enumerate(points):
            dist = (x**2 + y**2) ** 0.5
            closestPoints.append((dist, i))

        heapq.heapify(closestPoints)

        i = 0
        res = []
        for i in range(k):
            _, i = heapq.heappop(closestPoints)
            res.append(points[i])

        return res
            

        
        