class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        if n == 1:
            return True
        nLen = math.floor(math.log10(n) + 1)

        digits = [0] * nLen

        for i in range(nLen):        
            digits[i] = math.floor(n % (10 ** (i + 1)) / (10 ** i))

        odds = [x for x in digits if x > 0 and x & 1 == 1]
        evens = [x for x in digits if x & 1 == 0]

        for i in range(len(evens)):
            digits.remove(evens[i])
            permutations = list(itertools.permutations(digits))
            for pm in permutations:
                if pm[0] == 0:
                    continue
                j = int("".join([str(x) for x in pm]) + str(evens[i]))
                if (j & (j-1) == 0) and j != 0:
                    return True
            digits.append(evens[i])

        return False
