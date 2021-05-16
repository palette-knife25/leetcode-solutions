#  https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_list = []
        while l1 is not None:
            l1_list.append(l1.val)
            l1 = l1.next

        l2_list = []
        while l2 is not None:
            l2_list.append(l2.val)
            l2 = l2.next

        res_list = l1_list + l2_list
        res_list.sort()

        if len(res_list) == 0:
            return None

        res_node = ListNode(res_list[-1])
        for num in reversed(res_list[:-1]):
            res_node = ListNode(val=num, next=res_node)

        return res_node

#####################################################################

l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))

sln = Solution()
res = sln.mergeTwoLists(l1=l1, l2=l2)

answer=[]
nxt = res
while nxt is not None:
    answer.append(nxt.val)
    nxt = nxt.next

print(answer)