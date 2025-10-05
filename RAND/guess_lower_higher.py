# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while right >= left:
            middle = (left+right)//2
            res = guess(middle)
            if res == -1:
                right = middle-1
            
            elif res == 1:
                left = middle +1

            else: 
                return middle

            
