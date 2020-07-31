# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

x = ListNode()
x.val = 9
x.next = 1
x.next = 2
print(x.val)
l = x.val
while True:
    
    print(x.next)
    if x.next:
        continue
    else:
        break