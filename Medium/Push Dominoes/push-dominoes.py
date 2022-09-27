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
