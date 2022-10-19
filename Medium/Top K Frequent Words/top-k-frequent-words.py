class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        data = Counter(words)
        res = sorted(data.items(), key=lambda x: (-x[1], x[0]))
        return map(lambda x: x[0], res[:k])
