class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        debug = False

        for i in range(len(temperatures)):
            debug and print(stack)
            t = temperatures[i]
            if len(stack) == 0:
                stack.append(
                    (i, t)
                )
                continue
            if stack[-1][1] >= t:
                stack.append(
                    (i, t)
                )
                continue
            else:
                while stack and stack[-1][1] < t:
                    ix, _ = stack.pop()
                    res[ix] = i-ix
                stack.append(
                    (i, t)
                )

        return res
