
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closestPoints = []

        for i, (x, y) in enumerate(points):
            # Calculate squared distance from the origin
            dist = (x**2) + (y**2)

            # Add negative distance and original index to max-heap
            heapq.heappush(closestPoints, (-dist, i))

            # Remove farthest point if heap exceeds size k
            if len(closestPoints) > k:
                heapq.heappop(closestPoints)

        res = []
        for i in range(k):
            # Retrieve original index of the closest remaining point
            _, index = heapq.heappop(closestPoints)
            res.append(points[index])

        return res
