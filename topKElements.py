class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        di = {}
        for e in nums:
            if e in di:
                di[e]+=1
            else:
                di[e] = 1
        l = [[] for _ in range(len(nums)+1)]


        for num, freq in di.items():
            l[freq].append(num)

        res = []

        for i in range(len(l)-1, -1 ,-1):
            for num in l[i]:
                res.append(num)
                if len(res) == k:
                    return res

s = Solution()
test = [1,2,1,2,1,2,3,1,3,2]
print(s.topKFrequent(test, 2))

