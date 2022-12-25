class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        nums.sort()
        qrs = sorted(queries)
        res = []
        answers = {}

        for i in range(len(qrs)):
            q = qrs[i]
            pos = 0 if i == 0 else answers[qrs[i-1]][0]
            ans = 0 if i == 0 else answers[qrs[i-1]][1]
            for j in range(pos, len(nums)):
                if ans + nums[j] > q:
                    answers[q] = [j, ans]
                    break
                else: ans += nums[j]
            else:
                answers[q] = [j + 1, ans]
        
        for q in queries:
            res.append(answers[q][0])

        return res
