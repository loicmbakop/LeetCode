# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution(object):
#     def oddEvenList(self, head):
#         """
#         :type head: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """

#         even_indexes = []
#         odd_indexes = []
#         count = 0
#         itr = head
#         if head == None:
#             return
        
#         while itr:
#             if count%2 == 0: #even
#                 even_indexes.append(itr.val)
#             elif count %2==1: # odd
#                 odd_indexes.append(itr.val)
#             count+=1
#             itr = itr.next 
#         final_list =  even_indexes +odd_indexes 
#         new_node =  ListNode()
#         new_head = new_node
#         for element in final_list:
#             new_head.next = ListNode(element)
#             new_head = new_head.next

#         return new_node.next


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        odd = head
        even = head.next
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next
        
        odd.next = head.next
        return head


        

