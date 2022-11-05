from typing import List

class Node:

    def __init__(self, value):
        self.val = value
        self.children = []
        self.index = 0
    
    def insert(self, value):
        if value != self.val:
            n = Node(value)
            if value > self.val:
                n.index = self.index + 1
                if n.index == 2:
                    return True
            self.children.append(n)
        res = False
        for child in self.children:
            res = child.insert(value)
            if res:
                return True
        
        return False

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        if len(nums) < 3:
            return False

        node = Node(nums[0])
        node.is_root = True

        for n in nums[1:]:
            if node.insert(n):
                return True

        return False

def main():
    
    cases = [
        [
            [1,2,3,4,5],
            True
        ],
        [
            [5,4,3,2,1],
            False
        ],
        [
            [2,1,5,0,4,6],
            True
        ],
        [
            [1,5,0,4,1,3],
            True
        ]
    ]

    s = Solution()
    for case in cases:
        r = s.increasingTriplet(case[0])
        print(r)

if __name__ == "__main__":
    main()
