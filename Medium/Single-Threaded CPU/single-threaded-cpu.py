class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        queue = []

        for i, task in enumerate(tasks):
            heapq.heappush(
                queue,
                (task[0], task[1], i)
            )

        res = []
        acc = queue[0][0]
        group = []

        while queue or group:
            while queue and queue[0][0] <= acc:
                t = heapq.heappop(queue)
                tt = (t[1], t[2])
                heapq.heappush(group, tt)

            if group:
                task = heapq.heappop(group)
                res.append(task[1])
                acc += task[0]
            else:
                acc = queue[0][0]

        return res
