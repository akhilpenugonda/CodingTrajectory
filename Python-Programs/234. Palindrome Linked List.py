class Solution(object):
    def isPalindrome(self, head):
        if head is None:
            return True

        # Reverse the first half of the linked list
        def reverse_linked_list(node):
            prev = None
            while node:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
            return prev
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # If the length of the linked list is odd, move slow one step forward
        if fast:
            slow = slow.next

        # Reverse the second half of the linked list
        slow = reverse_linked_list(slow)

        # Compare the first and second halves
        while slow:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next

        return True
