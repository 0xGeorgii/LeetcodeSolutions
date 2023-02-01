class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        gcd = ""
        res = ""

        for i in range(min(len(str1), len(str2))):
            if str1[i] == str2[i]:
                gcd += str1[i]
            
            if str1.count(gcd) * len(gcd) == len(str1) and str2.count(gcd) * len(gcd) == len(str2):
                res = gcd if len(gcd) > len(res) else res

        return res
