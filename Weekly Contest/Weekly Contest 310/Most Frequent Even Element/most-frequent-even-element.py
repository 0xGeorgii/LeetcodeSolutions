class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return -1
        
        data = defaultdict(int)
        
        for i in range(len(nums)):
            n = nums[i]
            if n % 2 == 0:
                data[n] += 1
                
        if len(data) == 0:
            return -1
                
        data = dict(sorted(data.items(), key=lambda item: (-item[1], item[0] ) ))
        
        return list(data.keys())[0]
