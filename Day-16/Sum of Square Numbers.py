class Solution:
    import math
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, math.isqrt(c)  
        while left <= right:
            sum_squares = left * left + right * right
            if sum_squares == c:
                return True
            elif sum_squares < c:
                left += 1  
            else:
                right -= 1  
        return False
