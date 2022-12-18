class Solution:
    def calculate(self, s: str) -> int:
        vals = []
        ops = []
        data = []
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

        if len(set(s) & set(available_ops)) == 0:
            return int(s)

        def calc(op: str):
            a = vals.pop()
            b = vals.pop()
            vals.append(
                ops_funcs[op](b, a)
            )

        n = ""
        for i, c in enumerate(s):
            if c in available_ops:
                if len(n) > 0:
                    data.append(int(n))
                    n = ""
                data.append(c)
            else:
                n += c
        else:
            if len(n) > 0:
                data.append(int(n))
        
        for d in data:
            if d in available_ops:
                if len(ops) == 0:
                    ops.append(d)
                    continue
                if available_ops[d] <= available_ops[ops[-1]]:

                    while ops:
                        if available_ops[d] <= available_ops[ops[-1]]:
                            calc(ops.pop())
                        else:
                            break
                ops.append(d)
            else:
                vals.append(d)
        else:
            while ops: calc(ops.pop())

        return vals.pop()
