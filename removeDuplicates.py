class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<2:
            return
        i = 1
        tmp = nums[0]
        while i < len(nums):
            if nums[i]==tmp:
                del nums[i]
                continue
            tmp = nums[i]
            i += 1
        return