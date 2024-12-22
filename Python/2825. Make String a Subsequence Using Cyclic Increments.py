class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        
    
      
        p2 = 0 

        for x in range(len(str1)): 
            val1 = ord(str1[x])
            val2 = ord(str2[p2])
            if val1 == val2 or val1+1 == val2:
                p2+=1 
                if p2 == len(str2):
                    return True
            if val1==122 and val2==97:
                p2+=1 
                if p2 == len(str2):
                    return True

        return False




       
        #97-122
