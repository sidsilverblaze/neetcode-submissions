# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2=list2
        ans = None
        curr = ans
        while l1 and l2:

            if l1 and l2 and l1.val <=l2.val:
                if not ans:
                    ans = ListNode()
                    ans.val = l1.val
                    curr = ans
                else:
                    curr.next = ListNode(l1.val)
                    curr = curr.next
                l1 = l1.next
            else:
                if not ans:
                    ans = ListNode()
                    ans.val = l2.val
                    curr = ans
                else:
                    curr.next = ListNode(l2.val)
                    curr = curr.next
                l2 = l2.next
        if l1 :
            if curr:
                curr.next = l1
            else:
                ans = l1
        else:
            if curr:
                curr.next = l2
            else:
                ans = l2
        return ans


        