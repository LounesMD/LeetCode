class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        We double the divisor at each iteration so we can find the quotient faster.
        """
        sign = 1 
        if dividend < 0:
            sign *= -1
        if divisor < 0:
            sign *= -1

        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        
        while dividend >= divisor:
            d_divisor = divisor
            d_quotient = 1
            while dividend >= (d_divisor + d_divisor):
                d_divisor += d_divisor
                d_quotient += d_quotient
            dividend -= d_divisor
            quotient += d_quotient
        
        res = sign * quotient
        if res > 2**(31) - 1:
            return 2**(31) - 1 
        elif res < -2**31:
            return -2**31
        return res 
    
sol = Solution()
dividend = 2147483648
divisor = 3
print("res: ", sol.divide(dividend, divisor)) 