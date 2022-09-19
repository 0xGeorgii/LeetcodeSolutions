class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        data = defaultdict(list)
        
        for path in paths:
            segments = path.split(" ")
            root = segments[0]
            
            for file in segments[1:]:
                content = re.search("\([A-Za-z0-9]+\)", file).group(0)
                data[hash(content[1:-1])].append(root + "/" + file.replace(content, ""))
                
        res = list(filter(lambda x: len(x) > 1, data.values()))
        
        return res
