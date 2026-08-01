class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        temp = x
        reverse = 0
        while (temp > 0):
            digit = temp % 10
            reverse = reverse *10 + digit
            temp = temp//10
        if x == reverse:
            return True
        else:
            return False