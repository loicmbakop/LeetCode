class Solution():
    # def two_sum(self, arr, target):
    #     for i in range(len(arr)-1):
    #         for j in range(1, len(arr)-1):
    #             if arr[i] + arr[j] == target:
    #                 return(i, j)
    #     return -1

    def two_sum(self, arr, target):
        seen = {}
        for index, value in enumerate(arr):
            complement = target - value
            if complement in seen:
                return (index, seen[complement])
            seen[value] = index
        return -1
    
s = Solution()
l = [2, 6, 7, 9, 10]
print(s.two_sum(l, 9))


