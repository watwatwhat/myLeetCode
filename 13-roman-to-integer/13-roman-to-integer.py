class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum_ = 0
        dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

        for i in range(len(s[:-1])):
            if dict[s[i]] < dict[s[i+1]]:
                sum_ -= dict[s[i]]
            else:
                sum_ += dict[s[i]]
        return sum_ + dict[s[-1]]