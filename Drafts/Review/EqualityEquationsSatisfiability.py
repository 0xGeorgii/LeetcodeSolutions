from enum import Enum
from typing import List

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        parent = [i for i in range(26)]
        for e in equations:
            if e[1] == '=':
                parent[find(ord(e[0]) - ord('a'))] = find(ord(e[3]) - ord('a'))
        for e in equations:
            if e[1] == '!' and find(ord(e[0]) - ord('a')) == find(ord(e[3]) - ord('a')):
                return False
        return True

def main():
    solution = Solution()
    test_cases = [
        # [
        #     ["a==b","b!=a"], False
        # ],
        # [
        #     ["b==a","a==b"], True
        # ],
        # [
        #     ["c==c","b==d","x!=z"], True
        # ],
        # [
        #     ["a==b","b!=c","c==a"], False
        # ],
        # [
        #     ["a!=a"], False
        # ],
        # [
        #     ["f==d","b!=e","d!=c","b==c","b!=a","b!=f"], True
        # ],
        [
            ["a!=i","g==k","k==j","k!=i","c!=e","a!=e","k!=a","a!=g","g!=c"], True
        ]
    ]

    for test_case in test_cases:
        res = solution.equationsPossible(test_case[0])
        print(f"out: {res} exp: {test_case[1]}")

if __name__ == "__main__":
    main()
