class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        dominoes = list(dominoes)
        dl = len(dominoes)

        def check_condition(index, char):
            return  (
                    char == "L" and
                    index - 1 >= 0 and
                    dominoes[index-1] == "." and
                    (dominoes[index-2] != "R" if index - 2 >= 0 else True)
                ) or (
                    char == "R" and
                    index + 1 < dl and
                    dominoes[index+1] == "." and
                    (dominoes[index+2] != "L" if index + 2 < dl else True)
                )
            
        indexes = [i for i, x in enumerate(dominoes) if check_condition(i, x) ]

        while len(indexes) > 0:
            for i in indexes:
                dominoe = dominoes[i]

                if dominoe == "L":
                    dominoes[i-1] = dominoe
                elif dominoe == "R":
                    dominoes[i+1] = dominoe

            indexes = [i for i, x in enumerate(dominoes) if check_condition(i, x) ]
        return "".join(dominoes)

def main():
    
    test_cases =[
        [ "RR.L", "RR.L"],
        [ ".L.R...LR..L..", "LL.RR.LLRRLL.." ],
        [ ".L.R.", "LL.RR" ]
    ]

    # l = [i for i, x in enumerate(test_cases[1][0]) if x == "L" or x == "R"]

    solution = Solution()
    for tc in test_cases:
        res = solution.pushDominoes(tc[0])
        print("====")
        print(f"inp: {tc[0]}")
        print(f"out: {res}")
        print(f"exp: {tc[1]}")
        print(f"res: {res == tc[1]}")

if __name__ == "__main__":
    main()
