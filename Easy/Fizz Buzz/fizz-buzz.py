class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = list()
        for i in range(n):
            v = i + 1
            if v % 3 == 0 and v % 5 == 0:
                res.insert(i, "FizzBuzz")
            elif v % 3 == 0:
                res.insert(i, "Fizz")
            elif v % 5 == 0:
                res.insert(i, "Buzz")
            else:
                res.insert(i, str(v))
        return res
