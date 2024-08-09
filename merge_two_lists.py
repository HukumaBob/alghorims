# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. 
# The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to act as the head of the merged list
        dummy = ListNode()
        current = dummy
        
        # Traverse both lists and merge them
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # If there are remaining nodes in either list, append them
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        # Return the merged list, which starts at dummy.next
        return dummy.next


list1 = [1,2,4]
list2 = [1,3,4]
lists = Solution()
print(lists.mergeTwoLists(list1, list2))