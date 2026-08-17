class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n - 1):
            left_cnt = defaultdict(int)
            for l in range(i + 1):
                left_cnt[nums[l]] += 1

            right_cnt = defaultdict(int)
            for r in range(i + 1, n):
                right_cnt[nums[r]] += 1

            for num in left_cnt:
                if left_cnt[num] > (i + 1) // 2 and right_cnt[num] > (n - i - 1) // 2:
                    return i

        return -1