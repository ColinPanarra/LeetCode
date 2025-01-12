class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        nums = set(arr)

        for x in nums: 
            
            if x*2 in nums and x!=0:
                return True
            elif x==0:
                z = 0
                for n in arr:
                    if n==0:
                        z+=1
                if z>=2:
                    return True

                

        return False
        
