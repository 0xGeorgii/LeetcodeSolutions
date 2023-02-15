class Solution:
    def addToArrayForm(self, num1: List[int], k: int) -> List[int]:

        num2 = []

        for x in str(k):
            num2.append(int(x))

        ln1 = len(num1)
        ln2 = len(num2)

        if ln1 > ln2:
            num2 = [0] * (ln1-ln2) + num2
        elif ln2 > ln1:
            num1 = [0] * (ln2-ln1) + num1
        
        res = []

        num2 = num2[::-1]
        num1 = num1[::-1]
        m = 0

        for i in range(len(num1)):
            n1 = num1[i]
            n2 = num2[i]

            x = n1 + n2 + m

            if x < 10:
                res.append(x)
                m = 0
            else:
                res.append(x % 10)
                m = 1

        res = res[::-1]
        if m > 0:
            res = [ m ] + res
        
        return res
