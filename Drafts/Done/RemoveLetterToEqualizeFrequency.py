class Solution:
    def equalFrequency(self, word: str) -> bool:
        data = [0] * 26
        
        for c in word:
            data[ord(c) - ord('a')] += 1
            
        data = list(filter(lambda x: x != 0, data))

        for i in range(len(data)):
            d = list(data)
            d[i] -= 1
            if d[i] == 0:
                del d[i]
            if len(set(d)) <= 1:
                return True

        return False

def main():
    solution = Solution()
    cases = [
        [ "abcc", True ],
        [ "aazz", False ],
        [ "aaazzb", False ],
        [ "aaazzbb", True ],
        [ "bac", True],
        [ "ddaccb", False]
    ]
    for case in cases:
        res = solution.equalFrequency(case[0])
        print(f"out: {res} exp: {case[1]} -> {res == case[1]}")

if __name__ == "__main__":
    main()
