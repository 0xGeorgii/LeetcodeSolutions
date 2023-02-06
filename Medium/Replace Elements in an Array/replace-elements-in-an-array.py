class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        data = {}

        for i in range(len(nums)):
            data[nums[i]] = i
        
        for op in operations:
            i = data[op[0]]
            del data[op[0]]
            data[op[1]] = i
        
        res = []

        for k, v in dict(sorted(data.items(), key=lambda x: x[1])).items():
            res.append(k)
        
        return res
