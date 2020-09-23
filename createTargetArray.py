class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        returnList = []
        for i in range(len(index)):
            returnList.insert(index[i],nums[i])
        return returnList