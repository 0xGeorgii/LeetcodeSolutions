def is_palindrome(string) -> bool:
    return string == string[::-1]

class TrieNode:
    def __init__(self):
        self.children = {}
        self.palindromes_after = []
        self.index = -1
        
    def insert(self, string: str, index) -> bool:
        tmp = self
        for i, c in enumerate(string):
            if is_palindrome(string[i:]):
                tmp.palindromes_after.append(index)
            if c not in tmp.children:
                tmp.children[c] = TrieNode()
            tmp = tmp.children[c]

        if tmp.index >= 0:
            return False
        else:
            tmp.index = index
            return True

    def find_palindrome(self, string: str) -> List[int]:
        tmp = self
        res = []
        for i in range(len(string)):
            c = string[i]
            if tmp.index >= 0 and is_palindrome(string[i:]):
                res.append(tmp.index)
            if c not in tmp.children:
                break
            tmp = tmp.children[c]
        else:
            if tmp.index >= 0:
                res.append(tmp.index)
            res += tmp.palindromes_after
        
        return res

class Solution:    
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        node = TrieNode()

        for i in range(len(words)):
            node.insert(words[i][::-1], i)

        res = set()
        def dump_empty(index):
            for i in range(len(words)):
                if i == index or words[i] != words[i][::-1]:
                    continue
                res.add((i, index))
                res.add((index, i))
        
        for i in range(len(words)):
            word = words[i]
            if word == "":
                dump_empty(i)
                continue
            pi = node.find_palindrome(word)
            for p in pi:
                if p != i:
                    res.add((i, p))
        
        return list([list(i) for i in res])
