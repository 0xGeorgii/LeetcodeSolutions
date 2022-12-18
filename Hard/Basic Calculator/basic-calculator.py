class Solution:
    def calculate(self, s: str) -> int:

        vals = []
        ops = []
        data = []
        available_ops = {
             "+": 0,
             "-": 0,
             "N": 0,
             "*": 1,
             "/": 1,
             "^": 4,
             ")": 998,
             "(": 999
        }

        ops_funcs = {
            "+": lambda x,y: x + y,
            "-": lambda x,y: x - y,
            "N": lambda x: x * -1,
            "*": lambda x,y: x * y,
            "/": lambda x,y: int(x / y),
            "^": lambda x,y: x ** y
        }

        s = s.replace(" ", "")
        if len(set(s) & set(available_ops)) == 0:
            return int(s)

        def calc(op: str):
            if (op == "-" and len(vals) == 1) or op == "N":
                vals.append(ops_funcs["N"](vals.pop()))
            else:
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
                if c == "-" and s[i-1] in [ "+", "-", "("] and s[i+1] not in available_ops:
                    n = "-" + n
                    continue
                if c == "-" and s[i-1] == "(" and s[i+1] == "(":
                    data.append("N")
                    continue
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
                if d == ")":
                    while ops:
                        if ops[-1] != "(":
                            calc(ops.pop())
                        else:
                            ops.pop()
                            break
                    continue
                elif ops[-1] not in [ "(", ")"]:

                    while ops:
                        if available_ops[d] <= available_ops[ops[-1]] and ops[-1] not in [ "(", ")"]:
                            calc(ops.pop())
                        else:
                            break

                ops.append(d)
            else:
                vals.append(d)
        else:
            while ops:
                calc(ops.pop())

        return vals.pop()
