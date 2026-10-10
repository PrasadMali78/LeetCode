
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        diff.sort(reverse=True)
        diff.append(0)

        n = len(nums1)

        for i in range(n):
            count = i + 1
            needed = (diff[i] - diff[i + 1]) * count

            if k >= needed:
                k -= needed
            else:
                level = diff[i] - k // count
                remainder = k % count

                ans = sum(x * x for x in diff[i + 1:n])
                ans += (count - remainder) * level * level
                ans += remainder * (level - 1) * (level - 1)

                return ans

        return 0
