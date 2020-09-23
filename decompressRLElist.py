from collections import deque

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        returnList = deque([])
        i = 0
        while i < len(nums):
            returnList += deque([nums[i+1]]*nums[i])
            i += 2
        return returnList