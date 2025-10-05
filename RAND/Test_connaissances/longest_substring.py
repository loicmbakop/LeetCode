class solution:
    def longest_sub(self, s):
        # seen = set()
        # left = 0
        # longest_sub = 0
        # for right in range(len(s)-1):
        #     while s[right] in seen:
        #         seen.remove(s[left])
        #         left +=1
        #     seen.add(s[right])
        #     longest_sub = max(longest_sub, right-left+1)
        # return longest_sub


        seen = []
        longest_sub =0
        for e in s:
            if e in seen:
                seen = seen[seen.index(e)+1:]
            seen.append(e)
            longest_sub = max(longest_sub, len(seen))
        
        return longest_sub


s = solution()
test = "abcabcbb"
print(s.longest_sub(test))



