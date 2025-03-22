class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        hash = {}
        count = 0
        for e in arr:
            if e in hash:
                hash[e] += 1
            else: 
                hash[e] = 1

        checking_set = set()

        for e in hash:
            checking_set.add(hash[e])

        if len(checking_set)!= len(hash):
            return False
        else:
            return True
                
         


test = Solution()
test.uniqueOccurrences([1,2,2,1,1,3])