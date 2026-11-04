
from typing import List

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, v):
        i += 1
        while i <= self.n:
            self.bit[i] += v
            i += i & -i

    def query(self, i):
        s = 0
        while i:
            s += self.bit[i]
            i -= i & -i
        return s

    def kth(self, k):
        idx = 0
        mask = 1 << (self.n.bit_length() - 1)

        while mask:
            nxt = idx + mask
            if nxt <= self.n and self.bit[nxt] < k:
                idx = nxt
                k -= self.bit[nxt]
            mask >>= 1

        return idx


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        vals = sorted(set(nums))
        rank = {v: i for i, v in enumerate(vals)}
        a = [rank[v] for v in nums]

        m = len(vals)

        cnt = Fenwick(m)
        sm = Fenwick(m)

        window_sum = 0

        def update(i, delta):
            cnt.add(a[i], delta)
            sm.add(a[i], nums[i] * delta)

        def get_cost():
            mid = cnt.kth((x + 1) // 2)
            median = vals[mid]

            c = cnt.query(mid + 1)
            s = sm.query(mid + 1)

            return median * c - s + (window_sum - s) - median * (x - c)

        costs = []

        for i in range(x):
            update(i, 1)
            window_sum += nums[i]

        costs.append(get_cost())

        for i in range(x, n):
            update(i - x, -1)
            window_sum -= nums[i - x]

            update(i, 1)
            window_sum += nums[i]

            costs.append(get_cost())

        INF = float('inf')

        dp = [0] * (n + 1)

        for j in range(1, k + 1):
            ndp = [INF] * (n + 1)

            for i in range(1, n + 1):
                ndp[i] = ndp[i - 1]

                if i >= x:
                    ndp[i] = min(
                        ndp[i],
                        dp[i - x] + costs[i - x]
                    )

            dp = ndp

        return dp[n]
