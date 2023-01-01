class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        data = {}
        words = s.split()

        if len(pattern) != len(words):
            return False

        def is_under_another_letter(c, w):
            nonlocal data
            for k, v in data.items():
                if c == k: continue
                if v == w: return True
            return False

        for i, c in enumerate(pattern):
            w = words[i]

            if c not in data:
                if is_under_another_letter(c, w): return False
                data[c] = w
                continue
            elif data[c] != w or is_under_another_letter(c, w):
                return False

        return True
