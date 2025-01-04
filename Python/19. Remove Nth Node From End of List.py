# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        node1 = head
        size = 1
        while (node1.next):
            size+=1
            node1=node1.next
        
        removed_node = size - n 
        node2 = head

        if size==1:
            head = None
            return head 
        
        if removed_node == 0: 
            head = head.next
            return head
            
        for x in range(size-1):
            if x == removed_node-1:
                if node2.next.next:
                    node2.next = node2.next.next
                else:
                    node2.next = None
            else:
                node2=node2.next
        
        return head

        
