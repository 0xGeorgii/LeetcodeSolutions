class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[0])
        res = []

        for point in points:
            if len(res) == 0:
                res.append(point)
                continue
            if res[-1][1] >= point[0]:
                p = res.pop()
                res.append([max(p[0], point[0]), min(p[1], point[1])])
            else:
                res.append(point)

        return len(res)
