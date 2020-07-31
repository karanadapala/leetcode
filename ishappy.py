class Solutions(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        n = len(nums)
        #print(n)
        while n > 0:
            for i in range(0, 2**(len(nums)-n)):
                if len(nums[i:n+i])==0:
                    continue
                d[tuple(nums[i:n+i])] = sum(nums[i:n+i])
                print(nums[i:n+i])
            # print(n)
            n -=1
            # print(dict)
            # print(n)
        return max(d.values())
class Solution(object):
    def maxSubArray(self, nums):
        max_so_far = 0
        max_ending_here = 0
        if len(nums) == 1:
            return nums[0]
        else:
            for i in range(0, len(nums)): 
                max_ending_here = max_ending_here + nums[i] 
                
                if (max_so_far < max_ending_here): 
                    max_so_far = max_ending_here 
        
                if max_ending_here < 0: 
                    max_ending_here = 0   
            return max_so_far 

x = Solution()
print(x.maxSubArray([-1])) 


