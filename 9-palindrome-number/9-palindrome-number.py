class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            xStr = str(x)
            xStr_reversed = ''.join(list(reversed(xStr)))
            if xStr == xStr_reversed:
                return True
            else:
                return False