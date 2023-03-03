class Solution:
    def compress(self, chars: List[str]):

        stack = []
        res = ""

        for c in chars:
            if len(stack) == 0:
                stack.append((c, 0))
                continue
            cc, i = stack.pop()
            if cc == c:
                stack.append((cc, i + 1))
            else:
                res += cc + (str(i+1) if i > 0 else "")
                stack.append((c, 0))

        if stack:
            cc, i = stack.pop()
            res += cc + (str(i+1) if i > 0 else "")

        for i, c in enumerate(res):
            chars[i] = c

        return len(res)
