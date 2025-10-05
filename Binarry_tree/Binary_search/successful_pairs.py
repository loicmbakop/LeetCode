# class Solution(object):
#     def successfulPairs(self, spells, potions, success):
#         """
#         :type spells: List[int]
#         :type potions: List[int]
#         :type success: int
#         :rtype: List[int]
#         """

#         res = []
#         for i in spells:
#             count = 0
#             for j in potions :
                
#                 if i*j >= success:
#                     count +=1
#             res.append(count)

#         return res 


class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """

        potions.sort()
        res = []

        def bs(potions, target):
            left = 0
            right = len(potions) -1
            while left <= right:
                mid = (left + right)//2
                if potions[mid] < target:
                    left = mid +1 
                else :
                    right = mid 
                
            return left
            

        for spell in spells:
            index = bs(potions, success/spell)

            res.append(len(potions)-index)

        return res

    