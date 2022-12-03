class Solution:
    def frequencySort(self, s: str) -> str:

        characters = Counter(s)
        res = ""

        for k, v in sorted(characters.items(), key=lambda x: -x[1]):
            res += k * v

        return res
