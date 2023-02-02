class Solution:
    def isAlienSorted(self, words: List[str], lang: str) -> bool:
        for i in range(20):
            order, wtr = [], []
            for w in words:
                c = 0 if i >= len(w) else lang.index(w[i]) + 1
                order.append(c)
            if order != sorted(order): return False
            for j in range(len(order)-1, -1, -1):
                if order[j] > order[j-1]:
                    wtr.append(words[j])
            words = [ w for w in words if w not in wtr ]

        return True
