class Solution:
    def defangIPaddr(self, address: str) -> str:
        tmp = ""
        count = 0
        lastI = 0
        for i in range(len(address)):
            if address[i] == '.':
                if count == 2:
                    return tmp +'{}[.]{}'.format(address[lastI:i],address[i+1:])
                tmp += '{}[.]'.format(address[lastI:i])
                lastI = i+1
                count +=1