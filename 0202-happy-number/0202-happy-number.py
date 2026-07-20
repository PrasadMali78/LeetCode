class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n != 1:
            if n in visited:
                return False

            visited.add(n)

            sum_of_squares = 0

            while n > 0:
                digit = n % 10
                sum_of_squares += digit * digit
                n = n // 10

            n = sum_of_squares

        return True