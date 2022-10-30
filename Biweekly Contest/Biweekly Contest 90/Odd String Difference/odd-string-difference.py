class Solution:
    def oddString(self, words: List[str]) -> str:
        
        res = {}
        
        for word in words:
            arr = []
            
            for w in range(len(word) - 1):
                arr.append(ord(word[w+1]) - ord(word[w]))
            
            if tuple(arr) in res:
                res[tuple(arr)] = [ res[tuple(arr)][0] + 1, word]
            else:
                res[tuple(arr)] = [ 1 , word ]
            
        for k, v in res.items():
            if v[0] == 1:
                return v[1]
