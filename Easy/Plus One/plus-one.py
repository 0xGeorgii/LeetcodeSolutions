class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for n in range(len(digits) - 1, -1, -1):
            digits[n] += 1
            if (digits[n] > 9):
                digits[n] = 0
            else:
                return digits
            
        return [ 1 ] + digits
