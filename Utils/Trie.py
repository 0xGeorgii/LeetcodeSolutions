class Trie:        
    def __init__(self):
        self.children = {}
        self.is_terminal = False

    def print(self):
        def _print_rec(node, prefix):
            if node.is_terminal:
                print(prefix)

            for i in range(26):
                c = chr(i + 96)
                if c in node.children:
                    _print_rec(node.children[c], prefix + c)

        if self is None:
            print("Trie is empty")
            return
        _print_rec(self, "")

    def insert(self, string: str) -> Boolean:
        tmp = self
        for c in string:
            if c not in tmp.children:
                tmp.children[c] = TrieNode()
            tmp = tmp.children[c]
        
        if tmp.is_terminal:
            return False
        else:
            tmp.is_terminal = True
            return True

    def find(self, string: str) -> Boolean:
        tmp = self
        for c in string:
            if c not in tmp.children:
                return False
            else:
                tmp = tmp.children[c]
        return tmp.is_terminal
