class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        
        ev1Start = int(event1[0][:2]) * 60 + int(event1[0][3:])
        ev1End = int(event1[1][:2]) * 60 + int(event1[1][3:])
        
        ev2Start = int(event2[0][:2]) * 60 + int(event2[0][3:])
        ev2End = int(event2[1][:2]) * 60 + int(event2[1][3:])
        
        if len(list(set({ev1Start, ev1End}) & set({ev2Start, ev2End}))) > 0:
            return True

        if ev1Start < ev2Start:
            return ev2Start <= ev1End
        else:
            return ev1Start <= ev2End
