class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        @lru_cache(None)
        def dfs(r, c, balance):
            if balance < 0:
                return False

            if r == m - 1 and c == n - 1:
                return balance == 0

            if r + 1 < m:
                new_balance = balance + (1 if grid[r + 1][c] == '(' else -1)
                if dfs(r + 1, c, new_balance):
                    return True

            if c + 1 < n:
                new_balance = balance + (1 if grid[r][c + 1] == '(' else -1)
                if dfs(r, c + 1, new_balance):
                    return True

            return False

        return dfs(0, 0, 1)