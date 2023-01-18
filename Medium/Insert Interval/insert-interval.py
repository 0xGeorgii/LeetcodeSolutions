class Solution:
    def insert(self, intervals: List[List[int]], ni: List[int]) -> List[List[int]]:
        if len(intervals) == 0: return [ni]
        res = []
        inserted = False

        if ni[1] < intervals[0][0]:
            res.append(ni)
            inserted = True
        
        if ni[0] > intervals[-1][1]:
            intervals.append(ni)
            return intervals

        for j, interval in enumerate(intervals):

            if inserted:
                if interval[0] > res[-1][1]:
                    res.append(interval)
                else:
                    i = res.pop()
                    left = min(i[0], interval[0])
                    right = max(i[1], interval[1])
                    res.append([left, right])                    
            else:
                res.append(interval)
                if ni[0] > res[-1][1] and ni[1] < intervals[min(j+1, len(intervals)-1)][0]:
                    res.append(ni)
                    inserted = True
                    continue
                if ni[0] <= res[-1][0] <= ni[1] or ni[0] <= res[-1][1] <= ni[1]:
                    i = res.pop()
                    left = min(i[0], ni[0])
                    right = max(i[1], ni[1])
                    res.append([left, right])
                    inserted = True

        return res
