class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        ans=""
        for i in range(len(s)):
            for j in range(len(s)-1,i-1,-1):
                sub=s[i:j+1]
                if sub==sub[::-1]:
                    if len(sub)>len(ans):
                        ans=sub
                    break
        return ans                       

                                              
                


