class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:

        trees.sort()
        res = [trees[0]]
        max_p = trees[0]

        for i in range(len(trees)):            
            tree1 = max_p
            max_r = float("-inf")
            min_d = float("inf")

            for j in range(len(trees)):
                tree2 = trees[j]

                if tree2 in res or tree1 == tree2:
                    continue

                rad1 = math.atan2(tree1[1], tree1[0])
                rad2 = math.atan2(tree2[1], tree2[0])

                r = math.atan2(tree2[1]-tree1[1], tree2[0] - tree1[0])

                if r > max_r:
                    max_r = r
                    max_p = tree2
                    min_d =  math.sqrt(
                        pow(tree2[0] - tree1[0], 2) + pow(tree2[1] - tree1[1], 2)
                    )
                elif r == max_r:
                    d = math.sqrt(
                        pow(tree2[0] - tree1[0], 2) + pow(tree2[1] - tree1[1], 2)
                    )
                    if d < min_d:
                        max_r = r
                        max_p = tree2
                        min_d = d

                print(f"{tree1} - {tree2}: angle {r} dist {dist}")
            print(f"{tree1} - {tree2}: {max_p} angle {max_r}")
            res.append(max_p)
            print("=========")

        return res
