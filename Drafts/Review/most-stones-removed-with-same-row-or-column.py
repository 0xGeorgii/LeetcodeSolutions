class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        if len(stones) == 1:
            return 0

        def search(x):
            if data[x] != x:
                data[x] = search(data[x])
            return data[x]

        def touch(stone):
            x = stone[0]
            y = stone[1] + 10 ** 4

            if x not in data:
                data[x] = x
            if y not in data:
                data[y] = y

            rx = search(x)
            ry = search(y)

            data[rx] = ry

        data = {}

        for stone in stones:
            touch(stone)

        return len(stones) - len({search(d) for d in data})
