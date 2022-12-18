class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        vals = []
        available_ops = {
             "+": 0,
             "-": 0,
             "*": 1,
             "/": 1
        }

        ops_funcs = {
            "+": lambda x,y: x + y,
            "-": lambda x,y: x - y,
            "*": lambda x,y: x * y,
            "/": lambda x,y: int(x / y)
        }

        for t in tokens:

            if t in available_ops:
                a = vals.pop()
                b = vals.pop()
                vals.append(
                    ops_funcs[t](int(b), int(a))
                )                
            else:
                vals.append(t)

        return vals.pop()
