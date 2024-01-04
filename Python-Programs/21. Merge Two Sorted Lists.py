# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        current = dummy
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1 is not None:
            current.next = list1
        elif list2 is not None:
            current.next = list2
        return dummy.next


def printList(list):
    while list is not None:
        print(list.val, end=" ")
        list = list.next
    print()


def mergeTwoSortedLinkedlists(list1, list2):
    if list1 is None:
        return list2
    elif list2 is None:
        return list1
    elif list1.val <= list2.val:
        list1.next = mergeTwoSortedLinkedlists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoSortedLinkedlists(list1, list2.next)
        return list2
