class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        import math
        while b:
            a, b = b, a % b
        return a
    
    def check_division(s, t):
            return s == t * (len(s) // len(t))
        gcd_length = gcd(len(str1), len(str2))
        
        gcd_string = str1[:gcd_length]
        
        if check_division(str1, gcd_string) and check_division(str2, gcd_string):
            return gcd_string
        return ""

