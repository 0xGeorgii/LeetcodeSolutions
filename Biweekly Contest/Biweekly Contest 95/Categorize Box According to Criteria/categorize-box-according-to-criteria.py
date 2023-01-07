class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        
        
        isHeavy = mass >= 100        
        isBulky = length >= 1e4 or width >= 1e4 or height >= 1e4 or mass >= 1e4 or length * width * height >= 1e9
        
        if isHeavy and isBulky:
            return "Both"
        elif not isHeavy and not isBulky:
            return "Neither"
        elif isBulky and not isHeavy:
            return "Bulky"
        elif isHeavy and not isBulky:
            return "Heavy"
        
        return ""
