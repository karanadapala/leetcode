class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        count = 0
        # mean
        # two lists
        # if 0 < mean and 1 > mean status true and count
        # for i in range(0,len(nums)):
        #     if i != len(nums) -1:
        #         if nums[i]>nums[i+1]:
        #             if status:
        #                 count +=1
        #             continue
        # mean = float(sum(nums))/len(nums)
        # lesserThanMean = []
        # greaterThanMean = []
        if len(prices)==1:
            return prices[0]
        for i in range(0,len(prices)-1):
            l = prices[i+1]-prices[i]
            if l + count > count:
                count = l + count
            
        return count

x = Solution()
print(x.maxProfit([7,6,4,3,1])) 
