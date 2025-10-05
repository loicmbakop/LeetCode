class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = []
        longest_sub = 0
        for e in s:
            if e in seen:
                seen = seen[seen.index(e)+1:]
            seen.append(e)
            longest_sub = max(longest_sub, len(seen))
        return longest_sub

s = Solution()
t = 'abcabcbb'
s.lengthOfLongestSubstring(t)