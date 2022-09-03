class Solution:
    
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        if n == 1:
            return list(range(1, 10))
        
        if k == 0:
            res = []
            for i in range(1, 10, 1):                
                res.append(functools.reduce(lambda total, d: 10 * total + d, itertools.repeat(i, n), 0))
            return res

        res = list(range(1, 10))

        for level in range(n-1):
            next_digits = []
            for num in res:
                tail_digit = num % 10
                next_possible_digits = [tail_digit + k, tail_digit - k]

                for next_possible_digit in next_possible_digits:
                    if 0 <= next_possible_digit < 10:
                        next_digits.append(num * 10 + next_possible_digit)
                        
            res = next_digits

        return res
