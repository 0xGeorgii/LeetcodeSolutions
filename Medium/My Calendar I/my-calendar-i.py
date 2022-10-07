class MyCalendar:

    def __init__(self):
        self.events = []
        
    def book(self, start: int, end: int) -> bool:
        
        if len(self.events) == 0:
            self.events.append(
                (start, end)
            )
            
            return True
        
        for event in self.events:
            if (
                start < event[0] and end > event[0] 
            ) or event[0] <= start < event[1]:
                return False

        self.events.append(
            (start, end)
        )
        
        return True
