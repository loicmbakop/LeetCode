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
        
        while left <= right:
            middle = (left + right)//2
            res = guess(middle)
            if res == -1: # the guessed number is higher than the one we picked
                right = middle -1
            
            if res == 1: # the guessed number is lower than the one we picked
                left = middle +1

            if res == 0:
                return middle
