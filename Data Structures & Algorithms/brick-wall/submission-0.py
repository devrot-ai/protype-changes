class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n = len(wall)
        m = 0
        for brick in wall[0]:
            m += brick

        gaps = [[] for _ in range(n)]
        for i in range(n):
            gap = 0
            for brick in wall[i]:
                gap += brick
                gaps[i].append(gap)

        res = n
        for line in range(1, m):
            cuts = 0
            for i in range(n):
                if line not in gaps[i]:
                    cuts += 1

            res = min(res, cuts)
        return res