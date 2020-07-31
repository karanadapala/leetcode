class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = []
        for i in range(0,len(nums)):
            print(nums[i])
            if nums[i] == 0:
                l.append(i)
        count=0
        for k in l:
            nums.pop(k+count)
            nums.append(0)
            count -=1
        return nums

x = Solution()
print(x.moveZeroes([0,1,0,3,12])) 
