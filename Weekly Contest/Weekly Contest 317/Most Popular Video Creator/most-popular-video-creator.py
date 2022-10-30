class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:

        res = {}
        max_views = 0
        
        for i in range(len(creators)):
            
            if creators[i] in res:
                mnv = None
                mv = res[creators[i]][1]
                if views[i] > mv[1] or (views[i] == mv[1] and ids[i] < mv[0]):
                    mnv = [ ids[i], views[i] ]
                else:
                    mnv = mv
                    
                res[creators[i]] = ( res[creators[i]][0] + views[i], mnv )
                max_views = max(max_views, res[creators[i]][0])
            else:
                res[creators[i]] = ( views[i], [ ids[i], views[i] ] )
                max_views = max(max_views, views[i])
        
        
        ans = []
        
        for k, v in res.items():
            if v[0] == max_views:
                ans.append([k, v[1][0]])
        
        return ans
