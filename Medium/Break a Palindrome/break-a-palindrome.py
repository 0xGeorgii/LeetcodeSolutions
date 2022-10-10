class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        if len(palindrome) == 1:
            return ""
        
        for i, c in enumerate(palindrome):
            if c > "a":
                res = palindrome[:i] + "a" + palindrome[i+1:]
                if res == res[::-1]:
                    continue
                else:
                    return res
            if i == len(palindrome) - 1:
                nc = chr(ord(c) - 1) if c > "a" else chr(ord(c) + 1)
                return palindrome[:i] + nc + palindrome[i+1:]
                
        return ""
