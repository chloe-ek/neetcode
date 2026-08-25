class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []

        # points = [[0,2],[2,2]], k = 1
        for i in range(len(points)):
            point = points[i]
            
            distance = point[0]**2 + point[1]**2
            heapq.heappush(heap, (distance, point))

            # heap = [(4, [0, 2]), (8, [2, 2])]

        res = []

        for i in range(k):
            
            res.append(heapq.heappop(heap)[1])

        return res 

