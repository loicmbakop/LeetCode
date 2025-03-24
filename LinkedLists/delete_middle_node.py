# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution(object):
#     def deleteMiddle(self, head):
#         """
#         :type head: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """

#         if head == None:
#             print("empty linked list")
#             return None
        
#         if head.next == None:
#             return None
        
#         count = 0
#         itr = head
#         while itr:
#             count +=1
#             itr = itr.next
#         arr_size = count
#         middle_index = int(arr_size/2)

#         itr2 = head
#         count = 0
#         while itr2:
#             if count == middle_index-1:
#                 itr2.next = itr2.next.next
#                 break
#             count = count +1 
#             itr2 = itr2.next
        
#         return head

class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if head == None or head.next == None:
            return None
    
        arr = []
        itr = head
        while itr:
            arr.append(itr.val)
            itr = itr.next
    
        middle_index = len(arr)//2
        arr.pop(middle_index)

        new_head = ListNode()
        new_itr = new_head
        for e in arr:
            new_itr.next = ListNode(e)
            new_itr = new_itr.next
        return new_head.next


       

test = Solution()
test.deleteMiddle([1,3,4,7,1,2,6])
        
