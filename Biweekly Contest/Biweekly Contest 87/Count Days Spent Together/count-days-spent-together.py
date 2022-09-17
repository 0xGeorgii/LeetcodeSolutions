class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        
        month_to_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        arriveAlice_day = int(arriveAlice.split("-")[1])
        arriveAlice_month = int(arriveAlice.split("-")[0])
        
        arrive_alice_day_number = arriveAlice_day
        
        for i in range(0, arriveAlice_month - 1):
            arrive_alice_day_number += month_to_days[i]
                       
        
        leaveAlice_day = int(leaveAlice.split("-")[1])
        leaveAlice_month = int(leaveAlice.split("-")[0])
        
        leave_alice_day_number = leaveAlice_day
        
        for i in range(0, leaveAlice_month - 1):
            leave_alice_day_number += month_to_days[i]
        
        
        arriveBob_day = int(arriveBob.split("-")[1])
        arriveBob_month = int(arriveBob.split("-")[0])
        
        arrive_bob_day_number = arriveBob_day
        
        for i in range(0, arriveBob_month - 1):
            arrive_bob_day_number += month_to_days[i]
        
        leaveBob_day = int(leaveBob.split("-")[1])
        leaveBob_month = int(leaveBob.split("-")[0])
        
        leave_bob_day_number = leaveBob_day
        
        for i in range(0, leaveBob_month - 1):
            leave_bob_day_number += month_to_days[i]
            
        if arrive_alice_day_number > leave_bob_day_number or arrive_bob_day_number > leave_alice_day_number:
            return 0
        
        start = max(arrive_alice_day_number, arrive_bob_day_number)
        end = min(leave_alice_day_number, leave_bob_day_number)
            
        return end - start + 1
