class Solution:
    def canJump(self, nums: List[int]) -> bool:

        ln = len(nums)
        visited = set([0])
        queue = deque([0])

        while queue:
            index = queue.popleft()
            n = nums[index]
            if index + n + 1 >= ln: return True

            for i in range(index - n, index + n + 1):
                if i <= 0 or i >= ln or i in visited: continue
                visited.add(i)
                queue.append(i)
        
        return False
