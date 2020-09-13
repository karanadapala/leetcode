class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        maxCount = 0
        for i in nums:
            if i == 0:
                maxCount = max(maxCount,cnt)
                cnt = 0
            else:
                cnt += 1
        maxCount = max(maxCount,cnt)
        return maxCount