# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        cur_node = head
        met_nums = set()
        while cur_node:
            if cur_node in met_nums:
                return True
            met_nums.add(cur_node)
            cur_node = cur_node.next

        return False

#####################################################################

l1 = ListNode(3)
l1.next = ListNode(2)
l1.next.next = ListNode(0)
l1.next.next.next = ListNode(-4)
l1.next.next.next.next = l1.next

sln = Solution()
res = sln.hasCycle(head=l1)
print(res)