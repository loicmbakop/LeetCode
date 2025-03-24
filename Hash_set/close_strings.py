class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False
        set1 = set(word1)
        set2 = set(word2)

        d1 = {}
        d2 = {}

        for e in set1:
            if e not in set2:
                return False
            
        
        for e in word1:
            if e not in d1:
                d1[e] = 1
            else:
                d1[e] += 1

        for e in word2:
            if e not in d2:
                d2[e] = 1
            else:
                d2[e] += 1

        nbr_occur1 = []
        nbr_occur2 = []
        for e in d1:
            nbr_occur1.append(d1[e])
        for e in d2:
            nbr_occur2.append(d2[e])

        nbr_occur2.sort()
        nbr_occur1.sort()

        if nbr_occur1 != nbr_occur2:
            return False
        else:
            return True

    


test = Solution()
test.closeStrings("abc", "bca")

        