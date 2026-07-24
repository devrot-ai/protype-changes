class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def dfs(i, m):
            if i == n:
                return 0 if m == 0 else float("inf")
            if m == 0:
                return float("inf")

            res = float("inf")
            curSum = 0
            for j in range(i, n - m + 1):
                curSum += nums[j]
                res = min(res, max(curSum, dfs(j + 1, m - 1)))

            return res

        return dfs(0, k)