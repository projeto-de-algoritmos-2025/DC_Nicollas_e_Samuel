class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        
        ans = 1.0
        current_x = x 
        
        while n > 0:
            if n % 2 == 1:
                ans *= current_x
            current_x *= current_x
            n //= 2
            
        return ans