class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for i in strs:
            temp = i
            ls = sorted(temp)
            ls = ''.join(ls)
            if ls in d.keys():
                d[ls].append(i)
                d[ls]=sorted(d[ls],key=str.lower)
            else:
                d[ls] = [i]
        
        return sorted(list(d.values()),key=len)

x = Solution()
print(x.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) 