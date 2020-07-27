class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        d = {}
        count = 0
        #count all the occurrences in S
        for i in S:
            if i in d:
                d[i] +=1
            else:
                d[i]=1
        #add all the repititions based on the Jewels
        for j in J:
            if j in d:
                count += d[j]
        return count