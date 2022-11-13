class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True

        n = 0
        xl = int(log10(x))

        for i in range(xl+1):
            v = x % 10 ** (i+1)
            v = v // 10 ** i
            n += v * (10 ** (xl-i))

        return n == x
