class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        cnt = Counter(arr)
        al = len(arr)
        nl = len(arr)
        i = 0
        
        for k, v in cnt.most_common():
            i += 1
            nl -= v
            if al >= nl * 2:
                return i
