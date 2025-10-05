class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashmap = {}
        for e in nums:
                hashmap[e] = hashmap.get(e, 0) +1
               
        sorted_items = sorted(hashmap.items(), key=lambda x:x[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]
            


s = Solution()
l = [1,1,1,2,2,3]
s.topKFrequent(l, 2)