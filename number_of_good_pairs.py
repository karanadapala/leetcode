class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        #count the occurrences of elements
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        count = 0
        for j in d:
            #calculate the permutations
            #divide it by 2 so that the constraint i<j is met
            tmp = (d[j]*(d[j]-1))//2
            count += tmp
            
        return count