class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        tmp = -1
        out = 0
        for i in timeSeries:
            if out == 0:
                out += duration
                tmp=i
                continue
            if tmp+duration-1>=i:
                out += i-tmp
            else:
                out += duration
            tmp = i
        return out