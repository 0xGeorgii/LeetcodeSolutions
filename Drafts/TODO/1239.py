from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:

        al = len(arr)

        if al == 1:
            return len(arr[0]) if len(set(arr[0])) == len(arr[0]) else 0
        
        dp = [ [""] * (al + 1) for _ in range(al * al)]
        #arr.sort(key=len,reverse=True)
        res = -float("inf")
        x = -1
        for i in range(al * al):
            if i % ((al * al) // al) == 0:
                dp[i][0] = arr[i // al]
                x += 1
            for j, s2 in enumerate(arr):
                if dp[i][0] == '':
                    break
                if len(dp[i][j]) > 0:
                    continue

                tmp = dp[i][j-1] + s2
                if len(tmp) == len(set(tmp)):
                    dp[i][j] = tmp
                    dp[i][-1] = len(tmp)
                    res = max(res, len(tmp))
                else:
                    dp[i][j] = dp[i][j-1]
                    dp[i][-1] = len(dp[i][j-1])
                    res = max(res, len(dp[i][j-1]))

                tmp = dp[i][0] + s2
                if len(tmp) == len(set(tmp)):
                    dp[x * al + j][0] = tmp
                    #dp[j][-1] = len(tmp)
                    
        return res

def main():

    cases = [
        ["un","iq","ue"],
        ["cha","r","act","ers"],
        ["abcdefghijklmnopqrstuvwxyz"],
        ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"],
        ["ab","ba","cd","dc","ef","fe","gh","hg","ij","ji","kl","lk","mn","nm","op","po"],
        ["jnfbyktlrqumowxd","mvhgcpxnjzrdei"],
        ["aa","bb"],
        ["a", "abc", "d", "de", "def"],
        ["s","sa","m","e","mu","ei"],
        ["ab","cd","cde","cdef","efg","fgh","abxyz"]
    ]

    for case in cases:
        s = Solution()
        print(s.maxLength(case[0]))

if __name__ == "__main__":
    main()
