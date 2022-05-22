class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def is_palindrome(s):
            n = len(s)
            mid = n //2
            for i in range(mid):
                if s[i] != s[n - i -1]:
                    return False
            return True
        
        new_s = ""
        
        for c in s:
            c = c.lower()
            if c in "abcdefghijklmnopqrstuvwxyz0123456789":
                new_s += c
                
        return is_palindrome(new_s)