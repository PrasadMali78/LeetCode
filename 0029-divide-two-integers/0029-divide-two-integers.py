class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle overflow case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        # Determine the sign
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        # Repeatedly subtract the largest doubled divisor
        while dividend >= divisor:
            value = divisor
            count = 1

            while dividend >= (value << 1):
                value <<= 1
                count <<= 1

            dividend -= value
            quotient += count

        # Apply sign
        if negative:
            quotient = -quotient

        return quotient