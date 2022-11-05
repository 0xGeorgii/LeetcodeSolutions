from collections import defaultdict


class MyCalendar:
    def __init__(self):
        self.events = []
        self.intervals = defaultdict(int)

    def update_intervals(self, interval):
        for event in self.events:
            if (interval[0] <= event[0] and interval[1] > event[0]) or event[0] <= interval[0] < event[1]:
                self.intervals[interval] += 1

    def book(self, start: int, end: int) -> bool: 
        for event in self.events:
            
            if (start <= event[0] and end > event[0]) or event[0] <= start < event[1]:
                s = max(start, event[0])
                e = min(end, event[1])

                if (s, e) in self.intervals:
                    self.intervals[(s,e)] += 1
                else:
                    self.update_intervals((s,e))
                    self.intervals[(s,e)] += 1
                if self.intervals[(max(start, event[0]), min(end, event[1]))] >= 3:
                    return False

        self.events.append(
            (start, end)
        )
        self.intervals[(start, end)]+= 1
        
        return True


def main():

    cases = [
        [
            [
                [10,20],[50,60],[10,40],[5,15],[5,10],[25,55]
            ],
            [
                True,True,True,False,True,True
            ]
        ],
        [
            [
                [26,35],[26,32],[25,32],[18,26],[40,45],[19,26],[48,50],[1,6],[46,50],[11,18]
            ],
            [
                True,True,False,True,True,True,True,True,True,True
            ]
        ],
        [
            [
                [24,40],[43,50],[27,43],[5,21],[30,40],[14,29],[3,19],[3,14],[25,39],[6,19]
            ],
            [
                True,True,True,True,False,False,True,False,False,False
            ]
        ],
        [
            [
                [72,91],[53,66],[93,100],[87,98],[91,100],[96,100],[79,95],[33,48],[53,72],[55,74],[42,60],[67,82],[80,97],[2,15],[22,40],[46,62],[4,18],[50,60],[9,27],[79,94],[13,31],[67,81],[38,53],[14,25],[76,94],[1,20],[40,52],[12,28],[76,94],[75,88],[53,65],[85,98],[14,27],[97,100],[48,60],[25,43],[52,67],[33,46],[70,84],[12,26]
            ],
            [
                True,True,True,True,False,False,False,True,True,False,False,True,False,True,True,False,True,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False
            ]
        ]
    ]
    
    for j in range(3, len(cases)):
        case = cases[j]
        c = MyCalendar()

        for i, e in enumerate(case[0]):
            if e == [1, 20]:
                pass
            print(c.book(e[0], e[1]) == case[1][i])
    

if __name__ == "__main__":
    main()
