class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        r = reduce(lambda x, y: set(x).union(set(y)), board)
        if len(set(word).union(r)) > len(r):
            return False

        roots = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    roots.append(
                        (i,j)
                    )

        stack = []
        def try_add_to_stack(x, y, i):
            nonlocal stack
            if board[x][y] == word[i]:
                stack.append(
                    ((x, y), e[1] + word[i], e[2] + [(x,y)])
                )

        for root in roots:        
            stack = [ (root, word[0], [root]) ]
            while stack:
                e = stack.pop()
                (x,y) = e[0]
                if e[1] == word:
                    return True

                if x-1 >= 0 and (x-1, y) not in e[2]:
                    try_add_to_stack(x-1, y, len(e[1]))
                
                if x+1 < len(board) and (x+1, y) not in e[2]:
                    try_add_to_stack(x+1, y, len(e[1]))

                if y-1 >= 0 and (x, y-1) not in e[2]:
                    try_add_to_stack(x, y-1, len(e[1]))

                if y+1 < len(board[0]) and (x, y+1) not in e[2]:
                    try_add_to_stack(x, y+1, len(e[1]))

        return False
