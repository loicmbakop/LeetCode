# class Solution(object):
#     def findDifference(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[List[int]]
#         """
#         set1 = set(nums1)
#         set2 = set(nums2)
#         ans_0 = set([e for e in nums1 if e not in nums2])
#         ans_1 = set([e for e in nums2 if e not in nums1])
#         res = [list((ans_0)), list((ans_1))]

#         print(res)
#         return res
    




class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        in_l1_not_l2 = []
        in_l2_not_in_l1 = []
        for e in nums1:
            if e not in set2:
                in_l1_not_l2.append(e)
        for e in nums2:
            if e not in set1:
                in_l2_not_in_l1.append(e)

        return [in_l1_not_l2, in_l2_not_in_l1]
        

        
    
test = Solution()
test.findDifference([1,2,3,3], [1,1,2,2])




# test = Solution()
# test.findDifference([1,2,3,3], [1,1,2,2])