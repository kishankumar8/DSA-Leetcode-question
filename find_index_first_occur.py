class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        str=len(needle)

        str=len(haystack)
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len((needle))]==needle:
                return i

        return -1        

            
       