from typing import List

# TODO: see https://leetcode.com/problems/word-search-ii/solutions/712733/python-trie-solution-with-dfs-explained/?page=3

class Trie:

    def __init__(self):
        self.children = {}

    def add_children(self, chs: List[str]):
        def _find_children_rec(node, c):

            if len(node.children) == 0:
                return None
            
            if c in node.children:
                return node.children[c]
            else:
                for child in node.children.values():
                    return _find_children_rec(child, c)

        trie = self
        for ch in chs:
            child = _find_children_rec(trie, ch)
            if child == None:
                trie.children[ch] = Trie()
                child = trie.children[ch]
            trie = child

    def find(self, s):

        def _find_rec(node, c):
            if len(node.children) == 0:
                return None
            
            if c in node.children:
                return node.children[c]
            else:
                for child in node.children.values():
                    return _find_rec(child, c)

        trie = self
        for c in s:
            n = _find_rec(trie, c)

            if n == None:
                return False
            else:
                trie = n
        
        return True


    def print(self):
        def _print_rec(node, prefix):
            if len(node.children) == 0:
                print(prefix)

            for c in node.children:
                _print_rec(node.children[c], prefix + c)

        if self is None:
            print("Trie is empty")
            return

        _print_rec(self, "")

class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        bl = len(board)

        trie = Trie()

        for i in range(bl):
            for j in range(bl):


                if i + 1 < bl:
                    trie.add_children((board[i][j], board[i+1][j]))
                if i - 1 >= 0:
                    trie.add_children((board[i][j], board[i-1][j]))
                if j + 1 < bl:
                    trie.add_children((board[i][j], board[i][j+1]))
                if j - 1 >= 0:
                    trie.add_children((board[i][j], board[i][j-1]))
        
        for w in words:
            if trie.find(w):
                print(f"{w} is in the trie")
            else:
                print(f"{w} is not in the trie")
        return words


def main():

    cases = [      
        [  
            [
                ["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]
            ],
            ["oath","pea","eat","rain"]
        ]
    ]

    s = Solution()

    for case in cases:
        res = s.findWords(case[0], case[1])
        print(res)


if __name__ == "__main__":
    main()
