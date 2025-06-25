class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        dict = {}
        if x<0:
            return False
        else:
            size = len(str(x))
            for i in range(1,size+1):
                dict[i] = (x%(10**i)) // (10**(i-1)) #2345 becomes {1:5,2:4,3:3,4:2}
            for i in range(1,size+1):
                if dict[i] != dict[size-i+1]:
                    return False
            return True