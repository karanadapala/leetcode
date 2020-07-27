class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxVal = max(candies)
        l = []
        for i in candies:
            if i+extraCandies >= maxVal:
                l.append(True)
            else:
                l.append(False)
        return l