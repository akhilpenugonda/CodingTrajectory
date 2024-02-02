# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # iterating through all the linked lists and adding the elements to a list
        all_nodes = []
        for l in lists:
            while l:
                all_nodes.append(l.val)
                l = l.next
        # sorting the list
        all_nodes.sort()
        # creating a new linked list with the sorted elements
        head = ListNode(0)
        current = head
        for i in all_nodes:
            current.next = ListNode(i)
            current = current.next
        return head.next
    
# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         if not lists:
#             return None
#         if len(lists) == 1:
#             return lists[0]
        
#         mid = len(lists) // 2
#         left = self.mergeKLists(lists[:mid])
#         right = self.mergeKLists(lists[mid:])
        
#         return self.merge(left, right)
    
#     def merge(self, l1, l2):
#         dummy = ListNode(0)
#         curr = dummy
        
#         while l1 and l2:
#             if l1.val < l2.val:
#                 curr.next = l1
#                 l1 = l1.next
#             else:
#                 curr.next = l2
#                 l2 = l2.next
#             curr = curr.next
        
#         curr.next = l1 or l2
        
#         return dummy.next