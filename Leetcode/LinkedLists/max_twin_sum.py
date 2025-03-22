# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution(object):
#     def pairSum(self, head):
#         itr = head
#         count = 0
#         while itr:
#             count = count+1
#             itr = itr.next
#         ll_size = count


#         count2 = 0
#         itr = head
#         first_half = head
#         while count2 < ll_size//2-1:
#             itr = itr.next
#             count2+=1
#         second_half = itr.next
#         itr.next = None

#         curr = second_half
#         prev = None
#         while curr:
#             nex_node = curr.next
#             curr.next = prev
#             prev = curr
#             curr = nex_node
#         inverted_second_half = prev
#         itr_l1, itr_l2 = first_half, inverted_second_half
#         max_sum = 0
#         while itr_l1 and itr_l2:
#             maximum_temp = itr_l1.val + itr_l2.val
#             max_sum = max(maximum_temp, max_sum)
#             itr_l2 = itr_l2.next
#             itr_l1 = itr_l1.next 
#         return max_sum
    
  
class Solution(object):
    def pairSum(self, head):
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        prev, curr = None, slow
        while curr:
            nex_node = curr.next
            curr.next = prev
            prev = curr
            curr = nex_node
        second_half = prev
        max_sum = 0
        first_half = head
        while second_half:
            max_sum = max(max_sum, first_half.val + second_half.val)
            first_half = first_half.next
            second_half = second_half.next
        
        return max_sum