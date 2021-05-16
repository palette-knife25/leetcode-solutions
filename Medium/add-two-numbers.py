#  https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = 0
        fact = 1
        cur_num = l1
        while cur_num is not None:
            num1 += cur_num.val * fact
            fact *= 10
            cur_num = cur_num.next

        num2 = 0
        fact = 1
        cur_num = l2
        while cur_num is not None:
            num2 += cur_num.val * fact
            fact *= 10
            cur_num = cur_num.next

        res_num = num1 + num2
        res_node = ListNode()
        cur_num = res_num
        cur_node = res_node
        while cur_num != 0:
            dig = cur_num % 10
            cur_num = cur_num // 10
            cur_node.val = dig
            if cur_num != 0:
                cur_node.next = ListNode()
                cur_node = cur_node.next
        return res_node

#####################################################################

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

sln = Solution()
res = sln.addTwoNumbers(l1=l1, l2=l2)

answer=[]
nxt = res
while nxt is not None:
    answer.append(nxt.val)
    nxt = nxt.next

print(answer)