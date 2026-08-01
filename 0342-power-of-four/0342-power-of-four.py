class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n <= 0 :
            return False

        power = 1

        while (power < n ):
            power = power * 4

        if power == n :
            return True
        else:
            return False