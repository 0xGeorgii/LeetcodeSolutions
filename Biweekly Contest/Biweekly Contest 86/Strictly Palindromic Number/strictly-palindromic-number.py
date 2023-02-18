class Solution:
    def isStrictlyPalindromic(self, num: int) -> bool:

        def convert(n, b):
            if n == 0:
                return [0]
            digits = ""
            while n:
                digits += str(int(n % b))
                n //= b

            return digits

        for x in range(2, num-1):
            v = convert(num, x)
            if v != v[::-1]:
                return False
        
        return True
