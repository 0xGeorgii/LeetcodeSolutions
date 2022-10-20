class Solution:
    def intToRoman(self, num: int) -> str:

        def num_to_roman(n: int):
            if n >= 1000:
                return "M" * (n // 1000)
            elif 800 < n <= 1000:
                return ("C" * ((1000 - n) // 100)) + "M"
            elif 500 < n <= 800:
                return "D" + ("C" * ((n - 500) // 100 ))
            elif n == 500:
                return "D"
            elif 300 < n < 500:
                return ("C" * ((500 - n) // 100)) + "D"
            elif 100 <= n <= 300:
                return "C" * (n // 100)
            elif 80 < n < 100:
                return ("X" * ((100 - n) // 10)) + "C"
            elif 50 < n <= 80:
                return "L" + ("X" * ((n - 50) // 10))
            elif n == 50:
                return "L"
            elif 30 < n < 50:
                return ("X" * ((50 - n) // 10)) + "L"
            elif 10 <= n <= 30:
                return "X" * (n // 10)
            elif n == 9:
                return "IX"
            elif 5 < n < 9:
                return "V" + ("I" * (n - 5) )
            elif n == 5:
                return "V"
            elif 3 < n < 5:
                return ("I" * (5 - n) ) + "V"
            else:
                return "I" * n
        
        res = ""

        for i in range(int(math.log10(num)), -1, -1):
            n = (num // 10**i) % 10 * 10 ** i
            s = num_to_roman(n)
            res = res + s
            
        return res
