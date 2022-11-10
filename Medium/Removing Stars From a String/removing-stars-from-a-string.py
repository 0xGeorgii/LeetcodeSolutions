class Solution:
    def removeStars(self, s: str) -> str:

        stack = []

        for c in s:

            if len(stack) == 0:
                stack.append(c)
                continue

            if c == "*":                
                c1 = stack.pop()
                continue
            else:
                stack.append(c)

        return "".join(stack)
