class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack = []

        for c in s:

            if len(stack) == 0:
                stack.append(c)
                continue

            c1 = stack.pop()
            if c == c1:
                continue
            else:
                stack.append(c1)
                stack.append(c)
        
        return "".join(stack)
