# Given a string, find all possible palindromic partitions of given string.
# Input : nitin Output: n iti n, n i t i n, nitin

class Solution:
    # @param str, a string
    # @return a list of lists of string
    def partition(self, str):
        self.res=[]
        self.findPalindrome(str,[])
        return self.res

    def findPalindrome(self,str,plist):
        if len(str)==0: self.res.append(plist)
        for i in range(1,len(str)+1):
            if self.isPalindrome(str[:i]):
                self.findPalindrome(str[i:],plist+[str[:i]])

    def isPalindrome(self,str):
        if str==str[::-1]:
            return True
        else: 
            return False

if __name__ == '__main__':
    teststr = 'malayalam'
    print teststr
    sol = Solution()
    print sol.partition(teststr)
