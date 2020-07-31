class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        global count
        count = 0
        nums = sorted(nums)
        for i in nums:
            if count >= i:
                continue
            elif i-count ==1:
                count = i
            elif i-count>1:
                count= count+1
                return count
        return count+1
x = Solution()
print(x.firstMissingPositive([1,2,0])) 