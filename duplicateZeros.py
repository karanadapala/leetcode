class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i=0
        tmp = -1
        while i<len(arr):
            if i == tmp:
                i +=1
                continue
            if arr[i]==0:
                arr.insert(i+1, 0)
                del arr[-1]
                tmp = i+1
            i += 1
        return 