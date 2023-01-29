class Solution:
    
    def distinctIntegers(self, n: int) -> int:
        
        board = set([n])
        
        for _ in range(10**9 + 1):
            bl = len(board)
            ts = set()
            
            for x in board:
                for i in range(1, n+1):
                    if x % i == 1:
                        ts.add(i)
           
            board = board | ts
            if len(board) == bl:
                break
        
        return len(board)
