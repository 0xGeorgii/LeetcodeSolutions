class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        
        def compress_string():
            stack = [s[0]]
            ns = []

            for ch in s[1:]:
                c = stack.pop()
                if ch != c:
                    ns.append(c + (str(len(stack) + 1) if len(stack) > 0 else ""))
                    stack = []
                    stack.append(ch)
                else:
                    stack.append(c)
                    stack.append(ch)

            if len(stack) > 0:
                c = stack.pop()
                ns.append(c + (str(len(stack) + 1) if len(stack) > 0 else ""))

            return ns

        def compress_array(arr):
            to_del = []
            for i in range(0, len(arr)):
                if i > 0 and arr[i][:1] == arr[i-1][:1]:
                    arr[i-1] = arr[i-1][:1] + str(int(arr[i-1][:2]) + int(arr[i][2:]))
                    to_del.append(i)
                elif arr[i][2:] == "1":
                    arr[i] = arr[i][:1]

            for i in to_del:
                del arr[i]
            return arr

        def ns_len(arr):
            return sum(len(s) for s in arr)
            
        ns = compress_string()
        if k == 0:
            return ns
        
        dp = [ [ns[i]] * (k + 1) for i in range(len(ns))]
        
        for i in range(len(ns)):
            for j in range(1, k + 1):
                dp[i][j] = ns_len(ns) if int(dp[i][0][1:]) - j > 1 else ns_len(compress_array(ns))
        
        return len(ns)

def main():
    cases = [
        [ "aaabcccd", 2, 4 ]
    ]

    s = Solution()

    for case in cases:
        print(s.getLengthOfOptimalCompression(case[0], case[1]))

if __name__ == "__main__":
    main()
