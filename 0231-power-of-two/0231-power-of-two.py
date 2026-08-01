class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n <= 0:
            return False

        power = 1

        while power < n:
            power = power * 2

        return power == n